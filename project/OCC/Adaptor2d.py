# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _Adaptor2d.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Adaptor2d', [dirname(__file__)])
        except ImportError:
            import _Adaptor2d
            return _Adaptor2d
        if fp is not None:
            try:
                _mod = imp.load_module('_Adaptor2d', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Adaptor2d = swig_import_helper()
    del swig_import_helper
else:
    import _Adaptor2d
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Adaptor2d.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_Adaptor2d.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Adaptor2d.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Adaptor2d.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Adaptor2d.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Adaptor2d.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Adaptor2d.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Adaptor2d.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Adaptor2d.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Adaptor2d.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Adaptor2d.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Adaptor2d.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Adaptor2d.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Adaptor2d.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Adaptor2d.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Adaptor2d.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Adaptor2d.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _Adaptor2d.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.GeomAbs
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.gp
import OCC.Geom2d
import OCC.TColgp
class Adaptor2d_Curve2d(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def Delete(self):
        """
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Delete(self)

    def FirstParameter(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_Curve2d_FirstParameter(self)

    def LastParameter(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_Curve2d_LastParameter(self)

    def Continuity(self):
        """
        :rtype: GeomAbs_Shape

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Continuity(self)

    def NbIntervals(self, *args):
        """
        * If necessary, breaks the curve in intervals of continuity <S>. And returns the number of intervals.

        :param S:
        :type S: GeomAbs_Shape
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_Curve2d_NbIntervals(self, *args)

    def Intervals(self, *args):
        """
        * Stores in <T> the parameters bounding the intervals of continuity <S>.  The array must provide enough room to accomodate for the parameters. i.e. T.Length() > NbIntervals()

        :param T:
        :type T: TColStd_Array1OfReal &
        :param S:
        :type S: GeomAbs_Shape
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Intervals(self, *args)

    def Trim(self, *args):
        """
        * Returns a curve equivalent of <self> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>

        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Tol:
        :type Tol: float
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Trim(self, *args)

    def IsClosed(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_Curve2d_IsClosed(self)

    def IsPeriodic(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_Curve2d_IsPeriodic(self)

    def Period(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Period(self)

    def Value(self, *args):
        """
        * Computes the point of parameter U on the curve.

        :param U:
        :type U: float
        :rtype: gp_Pnt2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Value(self, *args)

    def D0(self, *args):
        """
        * Computes the point of parameter U on the curve.

        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_D0(self, *args)

    def D1(self, *args):
        """
        * Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.

        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V:
        :type V: gp_Vec2d
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_D1(self, *args)

    def D2(self, *args):
        """
        * Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.

        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V1:
        :type V1: gp_Vec2d
        :param V2:
        :type V2: gp_Vec2d
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_D2(self, *args)

    def D3(self, *args):
        """
        * Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.

        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V1:
        :type V1: gp_Vec2d
        :param V2:
        :type V2: gp_Vec2d
        :param V3:
        :type V3: gp_Vec2d
        :rtype: void

        """
        return _Adaptor2d.Adaptor2d_Curve2d_D3(self, *args)

    def DN(self, *args):
        """
        * The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.

        :param U:
        :type U: float
        :param N:
        :type N: Standard_Integer
        :rtype: gp_Vec2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_DN(self, *args)

    def Resolution(self, *args):
        """
        * Returns the parametric resolution corresponding  to the real space resolution <R3d>.

        :param R3d:
        :type R3d: float
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Resolution(self, *args)

    def GetType(self):
        """
        * Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.

        :rtype: GeomAbs_CurveType

        """
        return _Adaptor2d.Adaptor2d_Curve2d_GetType(self)

    def Line(self):
        """
        :rtype: gp_Lin2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Line(self)

    def Circle(self):
        """
        :rtype: gp_Circ2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Circle(self)

    def Ellipse(self):
        """
        :rtype: gp_Elips2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Ellipse(self)

    def Hyperbola(self):
        """
        :rtype: gp_Hypr2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Hyperbola(self)

    def Parabola(self):
        """
        :rtype: gp_Parab2d

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Parabola(self)

    def Degree(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Degree(self)

    def IsRational(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_Curve2d_IsRational(self)

    def NbPoles(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_Curve2d_NbPoles(self)

    def NbKnots(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_Curve2d_NbKnots(self)

    def NbSamples(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_Curve2d_NbSamples(self)

    def Bezier(self):
        """
        :rtype: Handle_Geom2d_BezierCurve

        """
        return _Adaptor2d.Adaptor2d_Curve2d_Bezier(self)

    def BSpline(self):
        """
        :rtype: Handle_Geom2d_BSplineCurve

        """
        return _Adaptor2d.Adaptor2d_Curve2d_BSpline(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Adaptor2d_Curve2d.Delete = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Delete,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.FirstParameter = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_FirstParameter,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.LastParameter = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_LastParameter,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Continuity = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Continuity,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.NbIntervals = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_NbIntervals,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Intervals = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Intervals,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Trim = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Trim,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.IsClosed = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_IsClosed,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.IsPeriodic = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_IsPeriodic,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Period = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Period,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Value = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Value,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.D0 = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_D0,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.D1 = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_D1,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.D2 = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_D2,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.D3 = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_D3,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.DN = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_DN,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Resolution = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Resolution,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.GetType = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_GetType,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Line = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Line,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Circle = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Circle,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Ellipse = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Ellipse,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Hyperbola = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Hyperbola,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Parabola = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Parabola,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Degree = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Degree,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.IsRational = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_IsRational,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.NbPoles = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_NbPoles,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.NbKnots = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_NbKnots,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.NbSamples = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_NbSamples,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.Bezier = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_Bezier,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d.BSpline = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d_BSpline,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d._kill_pointed = new_instancemethod(_Adaptor2d.Adaptor2d_Curve2d__kill_pointed,None,Adaptor2d_Curve2d)
Adaptor2d_Curve2d_swigregister = _Adaptor2d.Adaptor2d_Curve2d_swigregister
Adaptor2d_Curve2d_swigregister(Adaptor2d_Curve2d)

class Adaptor2d_HCurve2d(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def Curve2d(self):
        """
        * Returns a reference to the Curve2d inside the HCurve2d.

        :rtype: Adaptor2d_Curve2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Curve2d(self)

    def FirstParameter(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_FirstParameter(self)

    def LastParameter(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_LastParameter(self)

    def Continuity(self):
        """
        :rtype: GeomAbs_Shape

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Continuity(self)

    def NbIntervals(self, *args):
        """
        :param S:
        :type S: GeomAbs_Shape
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_NbIntervals(self, *args)

    def Intervals(self, *args):
        """
        :param T:
        :type T: TColStd_Array1OfReal &
        :param S:
        :type S: GeomAbs_Shape
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Intervals(self, *args)

    def Trim(self, *args):
        """
        * If <First> >= <Last>

        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Tol:
        :type Tol: float
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Trim(self, *args)

    def IsClosed(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_IsClosed(self)

    def IsPeriodic(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_IsPeriodic(self)

    def Period(self):
        """
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Period(self)

    def Value(self, *args):
        """
        :param U:
        :type U: float
        :rtype: gp_Pnt2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Value(self, *args)

    def D0(self, *args):
        """
        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_D0(self, *args)

    def D1(self, *args):
        """
        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V:
        :type V: gp_Vec2d
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_D1(self, *args)

    def D2(self, *args):
        """
        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V1:
        :type V1: gp_Vec2d
        :param V2:
        :type V2: gp_Vec2d
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_D2(self, *args)

    def D3(self, *args):
        """
        :param U:
        :type U: float
        :param P:
        :type P: gp_Pnt2d
        :param V1:
        :type V1: gp_Vec2d
        :param V2:
        :type V2: gp_Vec2d
        :param V3:
        :type V3: gp_Vec2d
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_D3(self, *args)

    def DN(self, *args):
        """
        :param U:
        :type U: float
        :param N:
        :type N: Standard_Integer
        :rtype: gp_Vec2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_DN(self, *args)

    def Resolution(self, *args):
        """
        :param R3d:
        :type R3d: float
        :rtype: float

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Resolution(self, *args)

    def GetType(self):
        """
        :rtype: GeomAbs_CurveType

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_GetType(self)

    def Line(self):
        """
        :rtype: gp_Lin2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Line(self)

    def Circle(self):
        """
        :rtype: gp_Circ2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Circle(self)

    def Ellipse(self):
        """
        :rtype: gp_Elips2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Ellipse(self)

    def Hyperbola(self):
        """
        :rtype: gp_Hypr2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Hyperbola(self)

    def Parabola(self):
        """
        :rtype: gp_Parab2d

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Parabola(self)

    def Degree(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Degree(self)

    def IsRational(self):
        """
        :rtype: bool

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_IsRational(self)

    def NbPoles(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_NbPoles(self)

    def NbKnots(self):
        """
        :rtype: int

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_NbKnots(self)

    def Bezier(self):
        """
        :rtype: Handle_Geom2d_BezierCurve

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_Bezier(self)

    def BSpline(self):
        """
        :rtype: Handle_Geom2d_BSplineCurve

        """
        return _Adaptor2d.Adaptor2d_HCurve2d_BSpline(self)

    def _kill_pointed(self):
        """_kill_pointed(Adaptor2d_HCurve2d self)"""
        return _Adaptor2d.Adaptor2d_HCurve2d__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(Adaptor2d_HCurve2d self) -> Handle_Adaptor2d_HCurve2d"""
        return _Adaptor2d.Adaptor2d_HCurve2d_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Adaptor2d_HCurve2d.Curve2d = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Curve2d,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.FirstParameter = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_FirstParameter,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.LastParameter = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_LastParameter,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Continuity = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Continuity,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.NbIntervals = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_NbIntervals,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Intervals = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Intervals,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Trim = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Trim,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.IsClosed = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_IsClosed,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.IsPeriodic = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_IsPeriodic,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Period = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Period,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Value = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Value,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.D0 = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_D0,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.D1 = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_D1,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.D2 = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_D2,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.D3 = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_D3,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.DN = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_DN,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Resolution = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Resolution,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.GetType = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_GetType,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Line = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Line,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Circle = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Circle,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Ellipse = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Ellipse,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Hyperbola = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Hyperbola,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Parabola = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Parabola,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Degree = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Degree,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.IsRational = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_IsRational,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.NbPoles = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_NbPoles,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.NbKnots = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_NbKnots,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.Bezier = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_Bezier,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.BSpline = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_BSpline,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d._kill_pointed = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d__kill_pointed,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d.GetHandle = new_instancemethod(_Adaptor2d.Adaptor2d_HCurve2d_GetHandle,None,Adaptor2d_HCurve2d)
Adaptor2d_HCurve2d_swigregister = _Adaptor2d.Adaptor2d_HCurve2d_swigregister
Adaptor2d_HCurve2d_swigregister(Adaptor2d_HCurve2d)

class Handle_Adaptor2d_HCurve2d(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _Adaptor2d.Handle_Adaptor2d_HCurve2d_swiginit(self,_Adaptor2d.new_Handle_Adaptor2d_HCurve2d(*args))
    DownCast = staticmethod(_Adaptor2d.Handle_Adaptor2d_HCurve2d_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_Adaptor2d_HCurve2d.Nullify = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HCurve2d_Nullify,None,Handle_Adaptor2d_HCurve2d)
Handle_Adaptor2d_HCurve2d.IsNull = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HCurve2d_IsNull,None,Handle_Adaptor2d_HCurve2d)
Handle_Adaptor2d_HCurve2d.GetObject = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HCurve2d_GetObject,None,Handle_Adaptor2d_HCurve2d)
Handle_Adaptor2d_HCurve2d._kill_pointed = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HCurve2d__kill_pointed,None,Handle_Adaptor2d_HCurve2d)
Handle_Adaptor2d_HCurve2d_swigregister = _Adaptor2d.Handle_Adaptor2d_HCurve2d_swigregister
Handle_Adaptor2d_HCurve2d_swigregister(Handle_Adaptor2d_HCurve2d)

def Handle_Adaptor2d_HCurve2d_DownCast(*args):
  return _Adaptor2d.Handle_Adaptor2d_HCurve2d_DownCast(*args)
Handle_Adaptor2d_HCurve2d_DownCast = _Adaptor2d.Handle_Adaptor2d_HCurve2d_DownCast

class Adaptor2d_HLine2d(Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param C:
        :type C: Adaptor2d_Line2d &
        :rtype: None

        """
        _Adaptor2d.Adaptor2d_HLine2d_swiginit(self,_Adaptor2d.new_Adaptor2d_HLine2d(*args))
    def Set(self, *args):
        """
        :param C:
        :type C: Adaptor2d_Line2d &
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_HLine2d_Set(self, *args)

    def ChangeCurve2d(self):
        """
        :rtype: Adaptor2d_Line2d

        """
        return _Adaptor2d.Adaptor2d_HLine2d_ChangeCurve2d(self)

    def _kill_pointed(self):
        """_kill_pointed(Adaptor2d_HLine2d self)"""
        return _Adaptor2d.Adaptor2d_HLine2d__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(Adaptor2d_HLine2d self) -> Handle_Adaptor2d_HLine2d"""
        return _Adaptor2d.Adaptor2d_HLine2d_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Adaptor2d_HLine2d.Set = new_instancemethod(_Adaptor2d.Adaptor2d_HLine2d_Set,None,Adaptor2d_HLine2d)
Adaptor2d_HLine2d.ChangeCurve2d = new_instancemethod(_Adaptor2d.Adaptor2d_HLine2d_ChangeCurve2d,None,Adaptor2d_HLine2d)
Adaptor2d_HLine2d._kill_pointed = new_instancemethod(_Adaptor2d.Adaptor2d_HLine2d__kill_pointed,None,Adaptor2d_HLine2d)
Adaptor2d_HLine2d.GetHandle = new_instancemethod(_Adaptor2d.Adaptor2d_HLine2d_GetHandle,None,Adaptor2d_HLine2d)
Adaptor2d_HLine2d_swigregister = _Adaptor2d.Adaptor2d_HLine2d_swigregister
Adaptor2d_HLine2d_swigregister(Adaptor2d_HLine2d)

class Handle_Adaptor2d_HLine2d(Handle_Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _Adaptor2d.Handle_Adaptor2d_HLine2d_swiginit(self,_Adaptor2d.new_Handle_Adaptor2d_HLine2d(*args))
    DownCast = staticmethod(_Adaptor2d.Handle_Adaptor2d_HLine2d_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_Adaptor2d_HLine2d.Nullify = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HLine2d_Nullify,None,Handle_Adaptor2d_HLine2d)
Handle_Adaptor2d_HLine2d.IsNull = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HLine2d_IsNull,None,Handle_Adaptor2d_HLine2d)
Handle_Adaptor2d_HLine2d.GetObject = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HLine2d_GetObject,None,Handle_Adaptor2d_HLine2d)
Handle_Adaptor2d_HLine2d._kill_pointed = new_instancemethod(_Adaptor2d.Handle_Adaptor2d_HLine2d__kill_pointed,None,Handle_Adaptor2d_HLine2d)
Handle_Adaptor2d_HLine2d_swigregister = _Adaptor2d.Handle_Adaptor2d_HLine2d_swigregister
Handle_Adaptor2d_HLine2d_swigregister(Handle_Adaptor2d_HLine2d)

def Handle_Adaptor2d_HLine2d_DownCast(*args):
  return _Adaptor2d.Handle_Adaptor2d_HLine2d_DownCast(*args)
Handle_Adaptor2d_HLine2d_DownCast = _Adaptor2d.Handle_Adaptor2d_HLine2d_DownCast

class Adaptor2d_Line2d(Adaptor2d_Curve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param P:
        :type P: gp_Pnt2d
        :param D:
        :type D: gp_Dir2d
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _Adaptor2d.Adaptor2d_Line2d_swiginit(self,_Adaptor2d.new_Adaptor2d_Line2d(*args))
    def Load(self, *args):
        """
        :param L:
        :type L: gp_Lin2d
        :rtype: None

        :param L:
        :type L: gp_Lin2d
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        return _Adaptor2d.Adaptor2d_Line2d_Load(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Adaptor2d_Line2d.Load = new_instancemethod(_Adaptor2d.Adaptor2d_Line2d_Load,None,Adaptor2d_Line2d)
Adaptor2d_Line2d._kill_pointed = new_instancemethod(_Adaptor2d.Adaptor2d_Line2d__kill_pointed,None,Adaptor2d_Line2d)
Adaptor2d_Line2d_swigregister = _Adaptor2d.Adaptor2d_Line2d_swigregister
Adaptor2d_Line2d_swigregister(Adaptor2d_Line2d)



