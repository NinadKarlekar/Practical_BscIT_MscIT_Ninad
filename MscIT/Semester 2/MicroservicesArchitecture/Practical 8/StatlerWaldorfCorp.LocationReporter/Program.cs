using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Configuration;
using System.IO;

namespace StatlerWaldorfCorp.LocationReporter
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
