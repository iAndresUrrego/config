# Create for Codint Dev

import os
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ---------- Windows Config ----------

    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.up()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),

    # will be to screen edge - window would shrink.
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.reload_config()),
    
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ---------- Apps Config ----------

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # VSCode
    ([mod], "c", lazy.spawn("code")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Rofi
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Thunar
    ([mod], "e", lazy.spawn("thunar")),

    #
    ([mod], "v", lazy.spawn("virtualbox")),

    # -------- Hardware Config ----------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

# ---------- Icons Class ----------

# 1.nf-dev-firefox
# 2.nf-cod-terminal
# 3.nf-cod-code
# 4.nf-cod-database
# 5.nf-fa-youtube_play
# 6.nf-mdi-office
# 7.nf-dev-windows
# 8.nf-fa-volume_up
# 9.nf-mdi-battery

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "
]]

for i,group in enumerate(groups):
    actual_key=str(i+1)
    keys.extend([
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
        ])

# ---------- Items ----------

tamano_barra_principal=22
tamano_barra_pantalla_secundaria=20
tamano_barra_pantalla_terciara=20
tamano_fuente=9
tamano_iconos=15
color_barra="#181818"
color_activo="#ffffff"
color_inactivo="#3C4048"
color_border="#FF884B"
color_verde="#B2B2B2"
color_azul="#B2B2B2"
color_morado="#B2B2B2"
color_rojo="#B2B2B2"
fuente_predeterminada="Mononoki Nerd Font"

def init_layout_conf_theme():
    return {
    'border_focus': color_barra,
    'border_normal': color_barra,
    'border_width': 1,
    'margin': 10
    }
layout_conf = init_layout_conf_theme()

layouts = [
    layout.Max(**layout_conf),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente_predeterminada,
    fontsize=tamano_fuente,
    padding=2,
)
extension_defaults = widget_defaults.copy()


def separador():
    return widget.Sep(
        linewidth=0,
        padding=5
    )

def powerline(fg, bg):
    return widget.TextBox(
        text="", # Icon: nf-oct-triangle_left
        fontsize=41,
        padding=-4,
        foreground=fg,
        background=bg
    )

def icon(text, fg, bg, fontsize=12):
    return widget.TextBox(
        text=text,
        fontsize=fontsize,
        foreground=fg,
        background=bg
    )

# ---------- Screen Primary ----------
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=color_activo,
                    inactive=color_inactivo,
                    font=fuente_predeterminada,
                    fontsize=tamano_iconos,
                    margin_y=3,
                    margin_x=0,
                    padding_y=2,
                    padding_x=1,
                    borderwidth=1,
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    # urgent_border=color_border,
                    this_current_screen_border=color_border,
                    # this_screen_border=color_border,
                    other_current_screen_border=color_border,
                    # other_screen_border=color_barra,
                    disable_drag=True
                ),
                separador(),
                widget.Prompt(),
                widget.WindowName(
                    foreground=color_border,
                    fontsize=10,
                    padding=5,
                ),
                powerline(color_verde, color_barra),
                icon("  ", color_barra, color_verde), # Icon: nf-fa-download
                widget.CheckUpdates(
                    background=color_verde,
                    colour_have_updates=color_barra,
                    colour_no_updates=color_barra,
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates'
                ),
                powerline(color_azul, color_verde),
                icon("  ", color_barra, color_azul), # Icon: nf-fa-feed
                widget.Net(background=color_azul, foreground=color_barra, interface='wlp2s0'),
                powerline(color_morado, color_azul),
                widget.CurrentLayoutIcon(background=color_morado, scale=0.65),
                widget.CurrentLayout(foreground=color_barra, background=color_morado, padding=5),
                powerline(color_rojo, color_morado),
                icon("  ", color_barra, color_rojo), # Icon: nf-mdi-calendar_clock
                widget.Clock(foreground=color_barra, background=color_rojo,format="%Y-%m-%d %a %I:%M %p"),
                powerline(color_barra, color_rojo),
                widget.Systray(background=color_barra, padding=5),
            ],
            tamano_barra_principal,
            background=color_barra,
        ),
    ),
    # ---------- Screen Secondary ----------
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=color_activo,
                    inactive=color_inactivo,
                    font=fuente_predeterminada,
                    fontsize=tamano_iconos,
                    margin_y=3,
                    margin_x=0,
                    padding_y=2,
                    padding_x=1,
                    borderwidth=1,
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    # urgent_border=color_border,
                    this_current_screen_border=color_border,
                    # this_screen_border=color_border,
                    other_current_screen_border=color_border,
                    # other_screen_border=color_border,
                    disable_drag=True
                ),
                separador(),
                widget.Prompt(),
                widget.WindowName(
                    foreground=color_border,
                    fontsize=10,
                    padding=5,
                ),
                powerline(color_verde, color_barra),
                icon("  ", color_barra, color_verde), # Icon: nf-fa-download
                widget.CheckUpdates(
                    background=color_verde,
                    colour_have_updates=color_barra,
                    colour_no_updates=color_barra,
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates'
                ),
                powerline(color_azul, color_verde),
                icon("  ", color_barra, color_azul), # Icon: nf-fa-feed
                widget.Net(background=color_azul, foreground=color_barra, interface='wlp2s0'),
                powerline(color_morado, color_azul),
                widget.CurrentLayoutIcon(background=color_morado, scale=0.65),
                widget.CurrentLayout(foreground=color_barra, background=color_morado, padding=5),
                powerline(color_rojo, color_morado),
                icon("  ", color_barra, color_rojo), # Icon: nf-mdi-calendar_clock
                widget.Clock(foreground=color_barra, background=color_rojo,format="%Y-%m-%d %a %I:%M %p"),
                powerline(color_barra, color_rojo),
            ],
            tamano_barra_pantalla_secundaria,
            background=color_barra,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
    "picom --no-vsync &",
    "nm-applet &",
    "feh --bg-fill /home/codint/Pictures/wallpapers/fantasma.jpg",
]

for x in autostart:
    os.system(x)
