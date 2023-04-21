using StatlerWaldorfCorp.EventProcessor.Events;

namespace StatlerWaldorfCorp.EventProcessor.Queues
{
    public delegate void MemberLocationRecordedEventReceivedDelegate(MemberLocationRecordedEvent evt);

    public interface IEventSubscriber
    {
        void Subscribe();
        void Unsubscribe();
        
        event MemberLocationRecordedEventReceivedDelegate MemberLocationRecordedEventReceived;
    }
}