package traffic_light;

public abstract class TrafficLightState {
    TrafficLight trafficLight;

    public TrafficLightState(TrafficLight trafficLight) {
        this.trafficLight = trafficLight;
    }

    public abstract void transition();
}
