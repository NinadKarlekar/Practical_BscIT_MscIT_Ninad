//Controllers/GlossaryController.cs
using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using System.IO;

namespace Glossary.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class GlossaryController : ControllerBase
    {
        private static List<GlossaryItem> Glossary = new List<GlossaryItem> {
            new GlossaryItem
            {
                Term = "HTML",
                Definition = "Hypertext Markup Language"
            },
            new GlossaryItem
            {
                Term = "MVC",
                Definition = "Model View Controller"
            },
            new GlossaryItem
            {
                Term = "OpenID",
                Definition = "An open standard for authentication"
            }
        };

        [HttpGet]
        public ActionResult<List<GlossaryItem>> Get()
        {
            return Ok(Glossary);
        }

        [HttpGet]
        [Route("{term}")]
        public ActionResult<GlossaryItem> Get(string term)
        {
            var glossaryItem = Glossary.Find(item =>
            item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));

            if (glossaryItem == null)
            {
                return NotFound();
            }
            else
            {
                return Ok(glossaryItem);
            }
        }

        [HttpPost]
        public ActionResult Post(GlossaryItem glossaryItem)
        {
            var existingGlossaryItem = Glossary.Find(item =>
            item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));

            if (existingGlossaryItem != null)
            {
                return Conflict("Cannot create the term because it already exists.");
            }
            else
            {
                Glossary.Add(glossaryItem);
                var resourceUrl = Path.Combine(Request.Path.ToString(), Uri.EscapeUriString(glossaryItem.Term));
                return Created(resourceUrl, glossaryItem);
            }
        }

        [HttpPut]
        public ActionResult Put(GlossaryItem glossaryItem)
        {
            var existingGlossaryItem = Glossary.Find(item =>
            item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));

            if (existingGlossaryItem == null)
            {
                return BadRequest("Cannot update a nont existing term.");
            }
            else
            {
                existingGlossaryItem.Definition = glossaryItem.Definition;
                return Ok();
            }
        }

        [HttpDelete]
        [Route("{term}")]
        public ActionResult Delete(string term)
        {
            var glossaryItem = Glossary.Find(item =>
            item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));

            if (glossaryItem == null)
            {
                return NotFound();
            }
            else
            {
                Glossary.Remove(glossaryItem);
                return NoContent();
            }
        }
    }
}
