using StatlerWaldorfCorp.EventProcessor.Events;

namespace StatlerWaldorfCorp.EventProcessor.Queues
{
    public interface IEventEmitter
    {
        void EmitProximityDetectedEvent(ProximityDetectedEvent proximityDetectedEvent);
    }
}