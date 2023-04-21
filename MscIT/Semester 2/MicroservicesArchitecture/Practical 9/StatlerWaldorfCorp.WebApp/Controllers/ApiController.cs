using Microsoft.AspNetCore.Mvc;
using StatlerWaldorfCorp.WebApp.Models;

namespace StatlerWaldorfCorp.WebApp.Controllers
{
    [Route("api/test")]
    public class ApiController : Controller
    {
        [HttpGet]
        public IActionResult GetTest()
        {
            return this.Ok(new StockQuote { Symbol = "API", Price = 9999 });
        }
    }
}
