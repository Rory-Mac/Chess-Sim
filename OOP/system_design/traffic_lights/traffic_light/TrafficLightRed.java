package traffic_light;

public class TrafficLightRed extends TrafficLightState {
    
    public TrafficLightRed(TrafficLight trafficLight) {
        super(trafficLight);
    }

    public void transition() {
        trafficLight.setState(new TrafficLightGreen(trafficLight));
    }
}
