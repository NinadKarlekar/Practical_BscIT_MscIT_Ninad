using System;
using StatlerWaldorfCorp.LocationReporter.Events;

namespace StatlerWaldorfCorp.LocationReporter.Models
{
    public class CommandEventConverter : ICommandEventConverter
    {
        public MemberLocationRecordedEvent CommandToEvent(LocationReport locationReport) 
        {
            MemberLocationRecordedEvent locationRecordedEvent = new MemberLocationRecordedEvent {
                Latitude = locationReport.Latitude,
                Longitude = locationReport.Longitude,
                Origin = locationReport.Origin,
                MemberID = locationReport.MemberID,
                ReportID = locationReport.ReportID,
                RecordedTime = DateTime.Now.ToUniversalTime().Ticks
            };

           return locationRecordedEvent;
        }
    }
}