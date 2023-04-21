using System;

namespace StatlerWaldorfCorp.EventProcessor.Location
{
    public class GpsUtility 
    {
        private const double C_EARTH = 40000.0;

        public double DegToRad(double angle)
        {
            return (Math.PI / 180) * angle;
        }

        /*
         * Returns the distance between two GPS coordinates in kilometers.         
         */
        public double DistanceBetweenPoints(GpsCoordinate point1, GpsCoordinate point2)
        {            
            double distance = 0.0;
        
        
            double lat1Rad = DegToRad(point1.Latitude);
            double long1Rad = DegToRad(point1.Longitude);
            double lat2Rad = DegToRad(point2.Latitude);
            double long2Rad = DegToRad(point2.Longitude);

            double longDiff = Math.Abs(long1Rad - long2Rad);

            if (longDiff > Math.PI)
            {
                longDiff = 2.0 * Math.PI - longDiff;
            }
        
            double angleCalculation =
                Math.Acos(
                    Math.Sin(lat2Rad) * Math.Sin(lat1Rad) +
                    Math.Cos(lat2Rad) * Math.Cos(lat1Rad) * Math.Cos(longDiff));

            distance = C_EARTH * angleCalculation / (2.0 * Math.PI);

            return distance;
        }
    }
}