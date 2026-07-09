package org.rafaelia.rll;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public final class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        int arch = KernelBridge.archDetect();
        int score = KernelBridge.kernelScore(7, 11);
        TextView view = new TextView(this);
        view.setText("RLL native runtime OK\narch=" + arch + "\nscore=" + score);
        setContentView(view);
    }
}
