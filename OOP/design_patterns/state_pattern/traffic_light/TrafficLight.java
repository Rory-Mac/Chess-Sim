package traffic_light;

public class TrafficLight {
    private TrafficLightState state = new TrafficLightRed(this);

    // Functions pertaining to state of traffic light (using state design pattern)
    public void setState(TrafficLightState state) {
        this.state = state;
    }

    public void transition() {
        state.transition();
    }
}
