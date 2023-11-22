import java.util.Date;
import java.util.ArrayList;
import traffic_light.TrafficLight;

public class TrafficLane {
    private ArrayList<Date> trafficeNotifications = new ArrayList<Date>();
    private TrafficLight connectedLights = new TrafficLight();

    // transition all traffic lights in lane
    public void transition() {
        connectedLights.transition();
    }

    // Functions pertaining to quantity of traffic experienced by traffic light
    public void notify(Date timestamp) {
        this.trafficeNotifications.add(0, timestamp);
    }

    public int totalTraffic(Date since) {
        int count = 0;
        for (int i = 0; i < trafficeNotifications.size(); i++) {
            if (!since.before(trafficeNotifications.get(i))) {
                break;
            }
            count += 1;
        }
        return count;
    }
}