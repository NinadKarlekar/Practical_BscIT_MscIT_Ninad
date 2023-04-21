using System;
using System.Collections.Generic;

namespace StatlerWaldorfCorp.EventProcessor.Location
{
    public interface ILocationCache
    {
        IList<MemberLocation> GetMemberLocations(Guid teamId);

        void Put(Guid teamId, MemberLocation memberLocation);
    }
}