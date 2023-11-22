package traffic_light;

public class TrafficLight {
    public TrafficLightState state = new TrafficLightRed(this);

    void setState(TrafficLightState state) {
        this.state = state;
    }

    public void changeState() {
        state.transition();
    }
}
