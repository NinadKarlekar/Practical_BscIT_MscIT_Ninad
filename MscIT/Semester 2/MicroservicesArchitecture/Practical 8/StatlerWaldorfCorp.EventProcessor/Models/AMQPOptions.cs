namespace StatlerWaldorfCorp.EventProcessor.Models
{
    public class AMQPOptions
    {
        public string Username { get; set; }
        public string Password { get; set; }
        public string VirtualHost { get; set; }
        public string HostName { get; set; }
        public string Uri { get; set; }
    }
}