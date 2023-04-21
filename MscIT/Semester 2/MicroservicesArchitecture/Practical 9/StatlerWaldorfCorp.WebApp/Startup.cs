using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Configuration;

namespace StatlerWaldorfCorp.WebApp
{
    public class Startup
    {
        public Startup(IHostingEnvironment env)
        {
            var builder = new ConfigurationBuilder()
                .SetBasePath(env.ContentRootPath)
                .AddEnvironmentVariables();

            Configuration = builder.Build();
        }

        public IConfiguration Configuration { get; set; }

        public void ConfigureServices(IServiceCollection services) {            
            services.AddMvc();
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
        {     
           loggerFactory.AddConsole();
           loggerFactory.AddDebug();       
           
           app.UseDeveloperExceptionPage();
           app.UseMvc(routes =>
           {
               routes.MapRoute("default",
                   template: "{controller=Home}/{action=Index}/{id?}");
           });
           app.UseStaticFiles();
        }
    }
}
