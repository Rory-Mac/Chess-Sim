package traffic_light;

public class TrafficLightGreen extends TrafficLightState {
    
    public TrafficLightGreen(TrafficLight trafficLight) {
        super(trafficLight);
    }

    public void transition() {
        trafficLight.setState(new TrafficLightYellow(trafficLight));
    }
}
