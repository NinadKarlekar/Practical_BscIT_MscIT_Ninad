using System;
using Newtonsoft.Json;

namespace StatlerWaldorfCorp.EventProcessor.Location
{
    public class MemberLocation
    {
        public Guid MemberID { get; set; }
        public GpsCoordinate Location { get; set; }

        public string ToJsonString()
        {
            return JsonConvert.SerializeObject(this);
        }

        public static MemberLocation FromJsonString(string json)
        {
            return JsonConvert.DeserializeObject<MemberLocation>(json);
        }
    }
}