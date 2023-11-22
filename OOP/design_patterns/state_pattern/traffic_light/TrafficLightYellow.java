package traffic_light;

public class TrafficLightYellow extends TrafficLightState {
    
    public TrafficLightYellow(TrafficLight trafficLight) {
        super(trafficLight);
    }

    public void transition() {
        trafficLight.setState(new TrafficLightRed(trafficLight));
    }
}
