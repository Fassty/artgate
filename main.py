from kivy.config import Config
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.behaviors import TouchRippleBehavior

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'shaped', 1)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        #Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            #We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


from kivy.factory import Factory
Factory.register('HoverBehavior', HoverBehavior)

from kivy.uix.button import Button


class StrokeButtonSmall(HoverBehavior, Button):
    stroke_width = 0.9
    stroke_radius = 17
    stroke_color = (0, 0, 0, .8)
    active = False

    def on_enter(self):
        if not self.active:
            self.canvas.before.children[0].a = 0.5
            print("I'm in")

    def on_leave(self):
        if not self.active:
            self.canvas.before.children[0].a = 0
            print("I'm out")

    def on_release(self):
        if not self.active:
            self.canvas.before.children[0].a = 0.5
            print("I'm in")

    def on_press(self):
        self.active = not self.active
        if self.active:
            self.canvas.before.children[0].a = 0.75
        else:
            self.canvas.before.children[0].a = 0


class StrokeButtonLarge(Button):
    stroke_width = 1.1
    stroke_radius = 20
    stroke_color = (0, 0, 0, 1)


class MainScreen(Widget):
    def slide_it(self, *args):
        val = args[1]
        if val == 0:
            self.slider_image = 'data/images/slider_cropped.png'
        else:
            self.slider_image = 'data/images/slider_cropped_flipped.png'


class ArtGateApp(App):

    def build(self):
        Window.size = (900, 500)
        Window.shape_image = 'data/images/window_mask900x500.png'
        Window.shape_mode = 'binalpha'
        return MainScreen()


if __name__ == '__main__':
    ArtGateApp().run()


