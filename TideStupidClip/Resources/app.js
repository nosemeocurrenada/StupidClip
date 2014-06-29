logger = Ember.Logger;

Ember.onerror = function(error) {
    logger.log(error);
    throw error;
};

App = Ember.Application.create({
    tray: null,
    ready: function() {
        logger.log("app is ready");
        var me = this;
        var tray = Ti.UI.addTray("app://app_logo.png", function() {
            me.trayClicked();
        });
        this.set("tray", tray);
        var w = Ti.UI.getMainWindow();
        w.addEventListener(Ti.UNFOCUSED, function() {
            me.lostFocus();
        });
        this.moveToCorner();
        this.hideWindow();
    },
    trayClicked: function() {
        logger.log("tray icon clicked");
        var w = Ti.UI.getMainWindow();
        if (w.isVisible()) {
            this.hideWindow();
        } else
        if (this.lostFocusRecently) {
            logger.log("have lost focus recently, not showing");
        } else {
            this.moveToCorner();
            this.showWindow();
        }
    },
    hideWindow: function() {
        logger.log("hidding window");
        var w = Ti.UI.getMainWindow();
        w.hide();
    },
    showWindow: function() {
        logger.log("showing window");
        var w = Ti.UI.getMainWindow();
        w.show();
        w.focus();
        w.setTopMost(true);
        setTimeout(function() {
            w.setTopMost(false);
        }, 80);
    },
    moveToCorner: function() {
        logger.log("moviendo ventana");
        var w = Ti.UI.getMainWindow();
        var width = w.getWidth();
        var height = w.getHeight();
        var wwidth = window.screen.width;
        var wheight = window.screen.height;
        w.moveTo(wwidth - width, wheight - height);
    },
    lostFocusRecently: false,
    lostFocus: function() {
        this.set("lostFocusRecently", true);
        logger.log("lost focus");
        var w = Ti.UI.getMainWindow();
        w.setTopMost(false);
        logger.log("hidding");
        w.hide();
        var me = this;
        setTimeout(function() {
            me.set("lostFocusRecently", false);
        }, 800);
    }
});

App.Router.map(function() {});


App.IndexRoute = Ember.Route.extend({
    model: function() {
        /*
        var m = App.TaskList.create();
        logger.log("modelo creado");
        return m;
        */
    },
    setupController: function(controller, m) {
        /*
        logger.log("seteando modelo del controlador");
        logger.debug("this is the controller: " + controller);
        logger.debug("model name: " + m.name);
        controller.set("model", m);
        */
    }
});

App.IndexController = Ember.Controller.extend({
    actions: {
        closeApp: function() {
            logger.log("closing app");
            Ti.UI.getCurrentWindow().close();
        },
        testPython: function() {
            logger.log("python test");
            var s = window.py.cmd("");
            alert(s);
        }
    }
});

//








// Widgets, TODO: cambiar a archivo separado

Ws = Em.Namespace.create();

Ws.FocusableTextField = Em.TextField.extend({
    didInsertElement: function() {
        this.$().focus();
    },
    focusOut: function() {
        logger.log("focused out");
        this.sendAction('lostFocus');
    },
    keyPress: function(e) {
        logger.log("key pressed");
        if (e.charCode == 13)
            this.sendAction('enterPress');
    }
});