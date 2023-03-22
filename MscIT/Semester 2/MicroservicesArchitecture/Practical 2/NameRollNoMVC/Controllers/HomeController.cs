using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NameRollNoMVC.Models;
namespace NameRollNoMVC.Controllers
{
    public class HomeController: Controller
    {
        public async Task < IActionResult > Index()
        {
            var model = new StockQuote
            {
                Name = "Ninad", RollNo = "22306A1012"
            };
            return View(model);
        }
    }
}