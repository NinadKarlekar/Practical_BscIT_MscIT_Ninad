using System;

namespace StatlerWaldorfCorp.LocationReporter.Services
{
    public interface ITeamServiceClient
    {
        Guid GetTeamForMember(Guid memberId);
    }
}