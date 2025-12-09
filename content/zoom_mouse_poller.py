from talon import actions, cron, app, Module
from .poller import Poller


class ZoomMousePoller(Poller):
    """Polls Talon's control zoom mode and shows a small HUD indicator.

    This poller is self-contained and only depends on the public HUD
    content builder API. It publishes a tiny status icon and a text
    panel with the message "Zoom Mouse On" while
    `actions.tracking.control_zoom_enabled()` is True and removes them
    when it becomes False.
    """
    content = None
    enabled = False
    _job = None
    _last_state = False

    def enable(self):
        if not self.enabled:
            self.enabled = True
            # Poll every 200ms for changes
            self._job = cron.interval("200ms", self._check_zoom)

    def disable(self):
        if self.enabled:
            self.enabled = False
            try:
                cron.cancel(self._job)
            except Exception:
                pass
            self._job = None
            self._last_state = False
            # Ensure we remove any published content
            if self.content:
                self.content.publish_event("status_icons", "zoom_mouse", "remove")
                self.content.publish_event("text", "zoom_mouse_text", "remove")

    def _check_zoom(self):
        try:
            zoom_on = bool(actions.tracking.control_zoom_enabled())
        except Exception:
            # If the API isn't available for any reason, treat as off
            zoom_on = False

        # No change -> do nothing
        if zoom_on == self._last_state:
            return

        self._last_state = zoom_on

        if not self.content:
            return

        if zoom_on:
            # Create a small status icon and a text panel
            status_icon = self.content.create_status_icon("zoom_mouse", "C:\\Users\\MPhil\\AppData\\Roaming\\talon\\user\\talon_hud\\themes\\_base_theme\\images\\magnify_thicker.png", "Zoom Mouse", "Zoom mouse is active")
            self.content.publish_event("status_icons", status_icon.topic, "replace", status_icon)

        else:
            self.content.publish_event("status_icons", "zoom_mouse", "remove")


def register_poller():
    # Keep alive so this poller is active at all times and automatically
    # shows/hides the widget based on Talon's zoom-mouse state.
    actions.user.hud_add_poller("zoom_mouse", ZoomMousePoller(), True)


app.register("ready", register_poller)


mod = Module()
@mod.action_class
class Actions:

    def hud_zoom_mouse_on():
        """Activate the zoom-mouse indicator"""
        actions.user.hud_activate_poller("zoom_mouse")

    def hud_zoom_mouse_off():
        """Deactivate the zoom-mouse indicator"""
        actions.user.hud_deactivate_poller("zoom_mouse")
