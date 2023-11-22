import java.util.concurrent.TimeUnit;
import java.util.Date;

public class Intersection {
    private final float defaultInterval = 500;
    private int switchIntervalLo = (int) defaultInterval;
    private int switchIntervalHi;
    private TrafficLane lane1 = new TrafficLane();
    private TrafficLane lane2 = new TrafficLane();

    public Intersection() {
        // move first traffic lane from red (default) to green, second traffic lane remains in default red state
        lane1.transition();
    }

    public void transition() {
        lane1.transition();
        lane2.transition();
    }

    public void updateSwitchInterval() {
        int lane1traffic = lane1.totalTraffic(new Date(System.currentTimeMillis() - TimeUnit.MINUTES.toMillis(5)));
        int lane2traffic = lane2.totalTraffic(new Date(System.currentTimeMillis() - TimeUnit.MINUTES.toMillis(5)));
        float trafficRatio;
        trafficRatio = lane1traffic <= lane2traffic ? lane1traffic / lane2traffic : lane2traffic / lane1traffic;
        switchIntervalHi = (int) (defaultInterval * trafficRatio);
    }
}
