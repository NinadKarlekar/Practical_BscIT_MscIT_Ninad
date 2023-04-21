using System.IO;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;


namespace StatlerWaldorfCorp.EventProcessor
{
    public class Program
    {
        public static void Main(string[] args)
        {
            IConfiguration config = new ConfigurationBuilder()
 				.AddCommandLine(args)
				.Build();

	    	var host = new WebHostBuilder()
				.UseKestrel()
				.UseStartup<Startup>()
				.UseContentRoot(Directory.GetCurrentDirectory())
				.UseConfiguration(config)
				.Build();

	    	host.Run();
        }
    }
}
