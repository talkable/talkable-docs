.. _android_sdk/overriding_defaults:
.. include:: /partials/common.rst

Overriding default behaviour
----------------------------

1. Create new activity in your app which extends `TalkableActivity` and override methods there. Example:

  .. code-block:: java

    import com.talkable.sdk.TalkableActivity;

    public class OverriddenTalkableActivity extends TalkableActivity {
        @Override
        public void copyToClipboard(String string) {
            super.copyToClipboard(string);

            Toast.makeText(this, "Text copied!", Toast.LENGTH_LONG).show();
        }
    }


2. Change activity in manifest:

  .. code-block:: xml

    <!-- From -->
    <activity android:name="com.talkable.sdk.TalkableActivity" />

    <!-- To -->
    <activity android:name=".OverriddenTalkableActivity" />

3. If you need some features like full-screen or other, you can do it same as with regular activity.

  .. code-block:: java

    public class OverriddenTalkableActivity extends TalkableActivity {
        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            getWindow().getDecorView().setSystemUiVisibility(
              View.SYSTEM_UI_FLAG_LAYOUT_STABLE
            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_FULLSCREEN
            | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
        }

        ...
    }


.. container:: hidden

   .. toctree::
