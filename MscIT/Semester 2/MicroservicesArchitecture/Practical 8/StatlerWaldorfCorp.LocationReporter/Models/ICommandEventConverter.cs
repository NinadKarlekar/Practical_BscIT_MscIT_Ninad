using StatlerWaldorfCorp.LocationReporter.Events;

namespace StatlerWaldorfCorp.LocationReporter.Models
{
    public interface ICommandEventConverter
    {
        MemberLocationRecordedEvent CommandToEvent(LocationReport locationReport); 
    }
}