(function() {
  var Application, Utils,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  window.DEMO = window.DEMO || {};

  Utils = {
    'transform': Modernizr.prefixed('transform').replace(/([A-Z])/g, (function(_this) {
      return function(str, m1) {
        return '-' + m1.toLowerCase();
      };
    })(this)).replace(/^ms-/, '-ms-'),
    'translate': (function(_this) {
      return function(x, y) {
        var tran, vals;
        tran = Modernizr.csstransforms3d ? 'translate3d' : 'translate';
        vals = Modernizr.csstransforms3d ? '(' + x + ', ' + y + ', 0)' : '(' + x + ', ' + y + ')';
        return tran + vals;
      };
    })(this)
  };

  Application = (function() {
    function Application() {
      this.update = bind(this.update, this);
      this.next = bind(this.next, this);
      this.previous = bind(this.previous, this);
      this.onKeyup = bind(this.onKeyup, this);
      DEMO.utils = Utils;
      this.$doc = $(document);
      this.$roller = $('.roller');
      this.$step = $('#steps li');
      this.$title = $('#titles li');
      this.min = 0;
      this.max = this.$step.length - 1;
      this.active_index = 0;
      this.$step.eq(this.active_index).addClass('active');
      this.$title.eq(this.active_index).addClass('active');
      this.observe();
    }

    Application.prototype.observe = function() {
      return this.$doc.on('keyup', this.onKeyup);
    };

    Application.prototype.onKeyup = function(e) {
      var kc;
      kc = e.keyCode;
      if (kc === 38) {
        e.preventDefault();
        this.previous();
      }
      if (kc === 40) {
        e.preventDefault();
        return this.next();
      }
    };

    Application.prototype.previous = function() {
      if (this.active_index > this.min) {
        this.active_index--;
        return this.update();
      }
    };

    Application.prototype.next = function() {
      if (this.active_index < this.max) {
        this.active_index++;
        return this.update();
      }
    };

    Application.prototype.update = function() {
      var y;
      y = -(this.active_index * 100);
      this.$roller.css(DEMO.utils.transform, DEMO.utils.translate(0, y + "%"));
      this.$step.removeClass('active');
      this.$title.removeClass('active');
      this.$step.eq(this.active_index).addClass('active');
      return this.$title.eq(this.active_index).addClass('active');
    };

    return Application;

  })();

  $(function() {
    return DEMO.instance = new Application();
  });

}).call(this);

$( document ).ready(function() {
  $('.trigger').on('click', function() {
     $('.modal-wrapper').toggleClass('open');
    $('.page-wrapper').toggleClass('blur-it');
     return false;
  });
});