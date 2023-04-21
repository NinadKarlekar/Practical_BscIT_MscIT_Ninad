using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using StatlerWaldorfCorp.RealityService.Location;

namespace StatlerWaldorfCorp.RealityService.Controllers
{
    [Route("api/reality")]
    public class RealityController : Controller
    {
        private ILocationCache locationCache;
        private ILogger logger;

        public RealityController(ILocationCache locationCache,
            ILogger<RealityController> logger) 
        {
            this.locationCache = locationCache;
            this.logger = logger;
        }

        [HttpGet("/teams/{teamId}/members")]
        public virtual IActionResult GetTeamMembers(Guid teamId)
        {
            return this.Ok(locationCache.GetMemberLocations(teamId));
        }

        [HttpPut("/teams/{teamId}/members/{memberId}")]
        public virtual IActionResult UpdateMemberLocation(Guid teamId, Guid memberId, [FromBody]MemberLocation memberLocation)
        {
            locationCache.Put(teamId, memberLocation);
            return this.Ok(memberLocation);
        }

        [HttpGet("/teams/{teamId}/members/{memberId}")]
        public virtual IActionResult GetMemberLocation(Guid teamId, Guid memberId)
        {
            return this.Ok(locationCache.Get(teamId, memberId));
        }
    }
}