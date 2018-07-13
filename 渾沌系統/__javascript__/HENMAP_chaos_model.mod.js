	(function () {
		var math = {};
		var __name__ = '__main__';
		__nest__ (math, '', __init__ (__world__.math));
		var Chaos = __class__ ('Chaos', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, A, c) {
				self.A = list ([]);
				self.c = list ([]);
				self.ax = list ([1, 1, 1]);
				self.dx = list ([0, 0, 0]);
				self.g = list ([]);
				self.h = list ([]);
				self.j = list ([]);
				self.count = 0;
				self.A = A;
				self.c = c;
				self.runModulation ();
			});},
			get setModulation () {return __get__ (this, function (self, ax, dx) {
				self.ax = ax;
				self.dx = dx;
				self.runModulation ();
			});},
			get runModulation () {return __get__ (this, function (self) {
				var ax = self.ax;
				var dx = self.dx;
				self.g.append (-(ax [0] / (ax [1] * ax [1])));
				self.g.append (((2 * ax [0]) * dx [1]) / (ax [1] * ax [1]));
				self.g.append ((-(0.1) * ax [0]) / ax [2]);
				self.g.append (ax [0] * ((1.76 - (dx [1] * dx [1]) / (ax [1] * ax [1])) + ((0.1 * ax [0]) * dx [2]) / ax [2]) + dx [0]);
				self.h.append (ax [1] / ax [0]);
				self.h.append (-(ax [1] * dx [0]) / ax [0] + dx [1]);
				self.j.append (ax [2] / ax [1]);
				self.j.append (-(ax [2] * dx [1]) / ax [1] + dx [2]);
			});},
			get runChaos () {return __get__ (this, function (self, k, x) {
				var t = list ([]);
				var g = self.g;
				var h = self.h;
				var j = self.j;
				if (k <= 1) {
					x [0] = self.ax [0] * x [0] + self.dx [0];
					x [1] = self.ax [1] * x [1] + self.dx [1];
					x [2] = self.ax [2] * x [2] + self.dx [2];
				}
				t.append (round (((g [0] * (x [1] * x [1]) + g [1] * x [1]) + g [2] * x [2]) + g [3], 6));
				t.append (round (h [0] * x [0] + h [1], 6));
				t.append (round (j [0] * x [1] + j [1], 6));
				return t;
			});},
			get runMaster () {return __get__ (this, function (self, k, x) {
				return self.runChaos (k, x);
			});},
			get runSlave () {return __get__ (this, function (self, k, x, Um) {
				var t = self.runChaos (k, x);
				if (k > 1) {
					t [0] = round ((t [0] + self.createUs (x)) + Um, 6);
				}
				return t;
			});},
			get createUk () {return __get__ (this, function (self, X, Y) {
				self.Um = self.createUm (X);
				self.Us = self.createUs (Y);
				return self.Um + self.Us;
			});},
			get createUm () {return __get__ (this, function (self, x) {
				var A = self.A;
				var c = self.c;
				var g = self.g;
				var h = self.h;
				var j = self.j;
				var Um = ((((((math.pow (x [1], 2) * g [0] + x [1] * g [1]) + x [2] * g [2]) + (x [0] * c [0]) * h [0]) + (x [1] * c [1]) * j [0]) - x [0] * A) - (x [1] * c [0]) * A) - (x [2] * c [1]) * A;
				return Um;
			});},
			get createUs () {return __get__ (this, function (self, y) {
				var A = self.A;
				var c = self.c;
				var g = self.g;
				var h = self.h;
				var j = self.j;
				var Us = ((((((-(math.pow (y [1], 2)) * g [0] - y [1] * g [1]) - y [2] * g [2]) - (y [0] * c [0]) * h [0]) - (y [1] * c [1]) * j [0]) + y [0] * A) + (y [1] * c [0]) * A) + (y [2] * c [1]) * A;
				return Us;
			});},
			get checkSync () {return __get__ (this, function (self, Us, Um) {
				var Um = round (Um, 4);
				var Us = round (Us, 4);
				if (Us + Um == 0) {
					self.count++;
					if (self.count >= 10) {
						return true;
					}
				}
				else {
					return false;
				}
			});},
			get show () {return __get__ (this, function (self) {
				print ('A= ', self.A, '\nc= ', self.c, '\ng= ', self.g, '\nh= ', self.h, '\nj=', self.j);
				// pass;
			});}
		});
		__pragma__ ('<use>' +
			'math' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Chaos = Chaos;
			__all__.__name__ = __name__;
		__pragma__ ('</all>')
	}) ();
