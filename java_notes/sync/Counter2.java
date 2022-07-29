package sync;

import java.util.concurrent.CountDownLatch;
import java.util.HashSet;

public class Counter2 {

    public volatile static Integer count = 0;

    private static HashSet<Integer> set = new HashSet<>();

    public synchronized static void inc() {
        try {
            Thread.sleep(1); // 延迟1毫秒

        } catch (InterruptedException e) { // catch住中断异常，防止程序中断
            e.printStackTrace();

        }
        count++;// count值自加1
        set.add(count);
    }

    public static void main(String[] args) throws InterruptedException {

        final CountDownLatch latch = new CountDownLatch(100);

        for (int i = 0; i < 100; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    Counter2.inc();
                    latch.countDown();
                }
            }).start();
        }
        latch.await();

        System.out.println(set.size());
        System.out.println(set);
        System.out.println("运行结果：" + Counter2.count);

    }
}
