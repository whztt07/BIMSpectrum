# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _Intrv.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Intrv', [dirname(__file__)])
        except ImportError:
            import _Intrv
            return _Intrv
        if fp is not None:
            try:
                _mod = imp.load_module('_Intrv', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Intrv = swig_import_helper()
    del swig_import_helper
else:
    import _Intrv
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
    __swig_destroy__ = _Intrv.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_Intrv.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Intrv.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Intrv.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Intrv.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Intrv.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Intrv.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Intrv.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Intrv.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Intrv.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Intrv.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Intrv.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Intrv.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Intrv.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Intrv.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Intrv.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Intrv.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _Intrv.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.TCollection
import OCC.MMgt
Intrv_Before = _Intrv.Intrv_Before
Intrv_JustBefore = _Intrv.Intrv_JustBefore
Intrv_OverlappingAtStart = _Intrv.Intrv_OverlappingAtStart
Intrv_JustEnclosingAtEnd = _Intrv.Intrv_JustEnclosingAtEnd
Intrv_Enclosing = _Intrv.Intrv_Enclosing
Intrv_JustOverlappingAtStart = _Intrv.Intrv_JustOverlappingAtStart
Intrv_Similar = _Intrv.Intrv_Similar
Intrv_JustEnclosingAtStart = _Intrv.Intrv_JustEnclosingAtStart
Intrv_Inside = _Intrv.Intrv_Inside
Intrv_JustOverlappingAtEnd = _Intrv.Intrv_JustOverlappingAtEnd
Intrv_OverlappingAtEnd = _Intrv.Intrv_OverlappingAtEnd
Intrv_JustAfter = _Intrv.Intrv_JustAfter
Intrv_After = _Intrv.Intrv_After
class Intrv_Interval(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param Start:
        :type Start: float
        :param End:
        :type End: float
        :rtype: None

        :param Start:
        :type Start: float
        :param TolStart:
        :type TolStart: Standard_ShortReal
        :param End:
        :type End: float
        :param TolEnd:
        :type TolEnd: Standard_ShortReal
        :rtype: None

        """
        _Intrv.Intrv_Interval_swiginit(self,_Intrv.new_Intrv_Interval(*args))
    def Start(self):
        """
        :rtype: float

        """
        return _Intrv.Intrv_Interval_Start(self)

    def End(self):
        """
        :rtype: float

        """
        return _Intrv.Intrv_Interval_End(self)

    def TolStart(self):
        """
        :rtype: Standard_ShortReal

        """
        return _Intrv.Intrv_Interval_TolStart(self)

    def TolEnd(self):
        """
        :rtype: Standard_ShortReal

        """
        return _Intrv.Intrv_Interval_TolEnd(self)

    def Bounds(self, *args):
        """
        :param Start:
        :type Start: float &
        :param TolStart:
        :type TolStart: Standard_ShortReal &
        :param End:
        :type End: float &
        :param TolEnd:
        :type TolEnd: Standard_ShortReal &
        :rtype: None

        """
        return _Intrv.Intrv_Interval_Bounds(self, *args)

    def SetStart(self, *args):
        """
        :param Start:
        :type Start: float
        :param TolStart:
        :type TolStart: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_SetStart(self, *args)

    def FuseAtStart(self, *args):
        """
        * ****+****--------------------> Old one  ****+****------------------------> New one to fuse  <<< <<<  ****+****------------------------> result

        :param Start:
        :type Start: float
        :param TolStart:
        :type TolStart: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_FuseAtStart(self, *args)

    def CutAtStart(self, *args):
        """
        * ****+****-----------> Old one  <----------**+** Tool for cutting  >>> >>> ****+****-----------> result

        :param Start:
        :type Start: float
        :param TolStart:
        :type TolStart: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_CutAtStart(self, *args)

    def SetEnd(self, *args):
        """
        :param End:
        :type End: float
        :param TolEnd:
        :type TolEnd: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_SetEnd(self, *args)

    def FuseAtEnd(self, *args):
        """
        * <---------------------****+**** Old one  <-----------------**+**  New one to fuse  >>> >>>  <---------------------****+**** result

        :param End:
        :type End: float
        :param TolEnd:
        :type TolEnd: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_FuseAtEnd(self, *args)

    def CutAtEnd(self, *args):
        """
        * <-----****+****  Old one  **+**------> Tool for cutting  <<< <<<  <-----****+****  result

        :param End:
        :type End: float
        :param TolEnd:
        :type TolEnd: Standard_ShortReal
        :rtype: None

        """
        return _Intrv.Intrv_Interval_CutAtEnd(self, *args)

    def IsProbablyEmpty(self):
        """
        * True if myStart+myTolStart > myEnd-myTolEnd  or if myEnd+myTolEnd > myStart-myTolStart

        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsProbablyEmpty(self)

    def Position(self, *args):
        """
        * True if me is Before Other  **-----------**** Other ***-----*   Before ***------------*  JustBefore ***-----------------*  OverlappingAtStart ***--------------------------*  JustEnclosingAtEnd ***-------------------------------------* Enclosing ***----*  JustOverlappingAtStart ***-------------*  Similar ***------------------------* JustEnclosingAtStart  ***-*  Inside  ***------*  JustOverlappingAtEnd  ***-----------------* OverlappingAtEnd  ***--------* JustAfter  ***---* After

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: Intrv_Position

        """
        return _Intrv.Intrv_Interval_Position(self, *args)

    def IsBefore(self, *args):
        """
        * True if me is Before Other ***----------------**  me  **-----------**** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsBefore(self, *args)

    def IsAfter(self, *args):
        """
        * True if me is After Other  **-----------**** me ***----------------**  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsAfter(self, *args)

    def IsInside(self, *args):
        """
        * True if me is Inside Other  **-----------****  me ***--------------------------**  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsInside(self, *args)

    def IsEnclosing(self, *args):
        """
        * True if me is Enclosing Other ***----------------------------**** me ***------------------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsEnclosing(self, *args)

    def IsJustEnclosingAtStart(self, *args):
        """
        * True if me is just Enclosing Other at start  ***---------------------------**** me ***------------------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustEnclosingAtStart(self, *args)

    def IsJustEnclosingAtEnd(self, *args):
        """
        * True if me is just Enclosing Other at End ***----------------------------**** me  ***-----------------****  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustEnclosingAtEnd(self, *args)

    def IsJustBefore(self, *args):
        """
        * True if me is just before Other ***--------****   me  ***-----------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustBefore(self, *args)

    def IsJustAfter(self, *args):
        """
        * True if me is just after Other  ****-------****  me ***-----------**  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustAfter(self, *args)

    def IsOverlappingAtStart(self, *args):
        """
        * True if me is overlapping Other at start ***---------------***  me  ***-----------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsOverlappingAtStart(self, *args)

    def IsOverlappingAtEnd(self, *args):
        """
        * True if me is overlapping Other at end  ***-----------** me ***---------------***  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsOverlappingAtEnd(self, *args)

    def IsJustOverlappingAtStart(self, *args):
        """
        * True if me is just overlapping Other at start ***-----------***  me ***------------------------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustOverlappingAtStart(self, *args)

    def IsJustOverlappingAtEnd(self, *args):
        """
        * True if me is just overlapping Other at end  ***-----------*  me ***------------------------** Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsJustOverlappingAtEnd(self, *args)

    def IsSimilar(self, *args):
        """
        * True if me and Other have the same bounds  *----------------***  me ***-----------------**  Other

        :param Other:
        :type Other: Intrv_Interval &
        :rtype: bool

        """
        return _Intrv.Intrv_Interval_IsSimilar(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Intrv_Interval.Start = new_instancemethod(_Intrv.Intrv_Interval_Start,None,Intrv_Interval)
Intrv_Interval.End = new_instancemethod(_Intrv.Intrv_Interval_End,None,Intrv_Interval)
Intrv_Interval.TolStart = new_instancemethod(_Intrv.Intrv_Interval_TolStart,None,Intrv_Interval)
Intrv_Interval.TolEnd = new_instancemethod(_Intrv.Intrv_Interval_TolEnd,None,Intrv_Interval)
Intrv_Interval.Bounds = new_instancemethod(_Intrv.Intrv_Interval_Bounds,None,Intrv_Interval)
Intrv_Interval.SetStart = new_instancemethod(_Intrv.Intrv_Interval_SetStart,None,Intrv_Interval)
Intrv_Interval.FuseAtStart = new_instancemethod(_Intrv.Intrv_Interval_FuseAtStart,None,Intrv_Interval)
Intrv_Interval.CutAtStart = new_instancemethod(_Intrv.Intrv_Interval_CutAtStart,None,Intrv_Interval)
Intrv_Interval.SetEnd = new_instancemethod(_Intrv.Intrv_Interval_SetEnd,None,Intrv_Interval)
Intrv_Interval.FuseAtEnd = new_instancemethod(_Intrv.Intrv_Interval_FuseAtEnd,None,Intrv_Interval)
Intrv_Interval.CutAtEnd = new_instancemethod(_Intrv.Intrv_Interval_CutAtEnd,None,Intrv_Interval)
Intrv_Interval.IsProbablyEmpty = new_instancemethod(_Intrv.Intrv_Interval_IsProbablyEmpty,None,Intrv_Interval)
Intrv_Interval.Position = new_instancemethod(_Intrv.Intrv_Interval_Position,None,Intrv_Interval)
Intrv_Interval.IsBefore = new_instancemethod(_Intrv.Intrv_Interval_IsBefore,None,Intrv_Interval)
Intrv_Interval.IsAfter = new_instancemethod(_Intrv.Intrv_Interval_IsAfter,None,Intrv_Interval)
Intrv_Interval.IsInside = new_instancemethod(_Intrv.Intrv_Interval_IsInside,None,Intrv_Interval)
Intrv_Interval.IsEnclosing = new_instancemethod(_Intrv.Intrv_Interval_IsEnclosing,None,Intrv_Interval)
Intrv_Interval.IsJustEnclosingAtStart = new_instancemethod(_Intrv.Intrv_Interval_IsJustEnclosingAtStart,None,Intrv_Interval)
Intrv_Interval.IsJustEnclosingAtEnd = new_instancemethod(_Intrv.Intrv_Interval_IsJustEnclosingAtEnd,None,Intrv_Interval)
Intrv_Interval.IsJustBefore = new_instancemethod(_Intrv.Intrv_Interval_IsJustBefore,None,Intrv_Interval)
Intrv_Interval.IsJustAfter = new_instancemethod(_Intrv.Intrv_Interval_IsJustAfter,None,Intrv_Interval)
Intrv_Interval.IsOverlappingAtStart = new_instancemethod(_Intrv.Intrv_Interval_IsOverlappingAtStart,None,Intrv_Interval)
Intrv_Interval.IsOverlappingAtEnd = new_instancemethod(_Intrv.Intrv_Interval_IsOverlappingAtEnd,None,Intrv_Interval)
Intrv_Interval.IsJustOverlappingAtStart = new_instancemethod(_Intrv.Intrv_Interval_IsJustOverlappingAtStart,None,Intrv_Interval)
Intrv_Interval.IsJustOverlappingAtEnd = new_instancemethod(_Intrv.Intrv_Interval_IsJustOverlappingAtEnd,None,Intrv_Interval)
Intrv_Interval.IsSimilar = new_instancemethod(_Intrv.Intrv_Interval_IsSimilar,None,Intrv_Interval)
Intrv_Interval._kill_pointed = new_instancemethod(_Intrv.Intrv_Interval__kill_pointed,None,Intrv_Interval)
Intrv_Interval_swigregister = _Intrv.Intrv_Interval_swigregister
Intrv_Interval_swigregister(Intrv_Interval)

class Intrv_Intervals(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Creates a void sequence of intervals.

        :rtype: None

        * Creates a sequence of one interval.

        :param Int:
        :type Int: Intrv_Interval &
        :rtype: None

        * Creates by copying an existing sequence of intervals.

        :param Int:
        :type Int: Intrv_Intervals &
        :rtype: None

        """
        _Intrv.Intrv_Intervals_swiginit(self,_Intrv.new_Intrv_Intervals(*args))
    def Intersect(self, *args):
        """
        * Intersects the intervals with the interval <Tool>.

        :param Tool:
        :type Tool: Intrv_Interval &
        :rtype: None

        * Intersects the intervals with the intervals in the sequence <Tool>.

        :param Tool:
        :type Tool: Intrv_Intervals &
        :rtype: None

        """
        return _Intrv.Intrv_Intervals_Intersect(self, *args)

    def Subtract(self, *args):
        """
        :param Tool:
        :type Tool: Intrv_Interval &
        :rtype: None

        :param Tool:
        :type Tool: Intrv_Intervals &
        :rtype: None

        """
        return _Intrv.Intrv_Intervals_Subtract(self, *args)

    def Unite(self, *args):
        """
        :param Tool:
        :type Tool: Intrv_Interval &
        :rtype: None

        :param Tool:
        :type Tool: Intrv_Intervals &
        :rtype: None

        """
        return _Intrv.Intrv_Intervals_Unite(self, *args)

    def XUnite(self, *args):
        """
        :param Tool:
        :type Tool: Intrv_Interval &
        :rtype: None

        :param Tool:
        :type Tool: Intrv_Intervals &
        :rtype: None

        """
        return _Intrv.Intrv_Intervals_XUnite(self, *args)

    def NbIntervals(self):
        """
        :rtype: int

        """
        return _Intrv.Intrv_Intervals_NbIntervals(self)

    def Value(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_Intervals_Value(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Intrv_Intervals.Intersect = new_instancemethod(_Intrv.Intrv_Intervals_Intersect,None,Intrv_Intervals)
Intrv_Intervals.Subtract = new_instancemethod(_Intrv.Intrv_Intervals_Subtract,None,Intrv_Intervals)
Intrv_Intervals.Unite = new_instancemethod(_Intrv.Intrv_Intervals_Unite,None,Intrv_Intervals)
Intrv_Intervals.XUnite = new_instancemethod(_Intrv.Intrv_Intervals_XUnite,None,Intrv_Intervals)
Intrv_Intervals.NbIntervals = new_instancemethod(_Intrv.Intrv_Intervals_NbIntervals,None,Intrv_Intervals)
Intrv_Intervals.Value = new_instancemethod(_Intrv.Intrv_Intervals_Value,None,Intrv_Intervals)
Intrv_Intervals._kill_pointed = new_instancemethod(_Intrv.Intrv_Intervals__kill_pointed,None,Intrv_Intervals)
Intrv_Intervals_swigregister = _Intrv.Intrv_Intervals_swigregister
Intrv_Intervals_swigregister(Intrv_Intervals)

class Intrv_SequenceNodeOfSequenceOfInterval(OCC.TCollection.TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param I:
        :type I: Intrv_Interval &
        :param n:
        :type n: TCollection_SeqNodePtr &
        :param p:
        :type p: TCollection_SeqNodePtr &
        :rtype: None

        """
        _Intrv.Intrv_SequenceNodeOfSequenceOfInterval_swiginit(self,_Intrv.new_Intrv_SequenceNodeOfSequenceOfInterval(*args))
    def Value(self):
        """
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_SequenceNodeOfSequenceOfInterval_Value(self)

    def _kill_pointed(self):
        """_kill_pointed(Intrv_SequenceNodeOfSequenceOfInterval self)"""
        return _Intrv.Intrv_SequenceNodeOfSequenceOfInterval__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(Intrv_SequenceNodeOfSequenceOfInterval self) -> Handle_Intrv_SequenceNodeOfSequenceOfInterval"""
        return _Intrv.Intrv_SequenceNodeOfSequenceOfInterval_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Intrv_SequenceNodeOfSequenceOfInterval.Value = new_instancemethod(_Intrv.Intrv_SequenceNodeOfSequenceOfInterval_Value,None,Intrv_SequenceNodeOfSequenceOfInterval)
Intrv_SequenceNodeOfSequenceOfInterval._kill_pointed = new_instancemethod(_Intrv.Intrv_SequenceNodeOfSequenceOfInterval__kill_pointed,None,Intrv_SequenceNodeOfSequenceOfInterval)
Intrv_SequenceNodeOfSequenceOfInterval.GetHandle = new_instancemethod(_Intrv.Intrv_SequenceNodeOfSequenceOfInterval_GetHandle,None,Intrv_SequenceNodeOfSequenceOfInterval)
Intrv_SequenceNodeOfSequenceOfInterval_swigregister = _Intrv.Intrv_SequenceNodeOfSequenceOfInterval_swigregister
Intrv_SequenceNodeOfSequenceOfInterval_swigregister(Intrv_SequenceNodeOfSequenceOfInterval)

class Handle_Intrv_SequenceNodeOfSequenceOfInterval(OCC.TCollection.Handle_TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_swiginit(self,_Intrv.new_Handle_Intrv_SequenceNodeOfSequenceOfInterval(*args))
    DownCast = staticmethod(_Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_Intrv_SequenceNodeOfSequenceOfInterval.Nullify = new_instancemethod(_Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_Nullify,None,Handle_Intrv_SequenceNodeOfSequenceOfInterval)
Handle_Intrv_SequenceNodeOfSequenceOfInterval.IsNull = new_instancemethod(_Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_IsNull,None,Handle_Intrv_SequenceNodeOfSequenceOfInterval)
Handle_Intrv_SequenceNodeOfSequenceOfInterval.GetObject = new_instancemethod(_Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_GetObject,None,Handle_Intrv_SequenceNodeOfSequenceOfInterval)
Handle_Intrv_SequenceNodeOfSequenceOfInterval._kill_pointed = new_instancemethod(_Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval__kill_pointed,None,Handle_Intrv_SequenceNodeOfSequenceOfInterval)
Handle_Intrv_SequenceNodeOfSequenceOfInterval_swigregister = _Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_swigregister
Handle_Intrv_SequenceNodeOfSequenceOfInterval_swigregister(Handle_Intrv_SequenceNodeOfSequenceOfInterval)

def Handle_Intrv_SequenceNodeOfSequenceOfInterval_DownCast(*args):
  return _Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_DownCast(*args)
Handle_Intrv_SequenceNodeOfSequenceOfInterval_DownCast = _Intrv.Handle_Intrv_SequenceNodeOfSequenceOfInterval_DownCast

class Intrv_SequenceOfInterval(OCC.TCollection.TCollection_BaseSequence):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        """
        :rtype: None

        """
        _Intrv.Intrv_SequenceOfInterval_swiginit(self,_Intrv.new_Intrv_SequenceOfInterval())
    def Clear(self):
        """
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_Clear(self)

    def Assign(self, *args):
        """
        :param Other:
        :type Other: Intrv_SequenceOfInterval &
        :rtype: Intrv_SequenceOfInterval

        """
        return _Intrv.Intrv_SequenceOfInterval_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: Intrv_SequenceOfInterval &
        :rtype: Intrv_SequenceOfInterval

        """
        return _Intrv.Intrv_SequenceOfInterval_Set(self, *args)

    def Append(self, *args):
        """
        :param T:
        :type T: Intrv_Interval &
        :rtype: None

        :param S:
        :type S: Intrv_SequenceOfInterval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_Append(self, *args)

    def Prepend(self, *args):
        """
        :param T:
        :type T: Intrv_Interval &
        :rtype: None

        :param S:
        :type S: Intrv_SequenceOfInterval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_Prepend(self, *args)

    def InsertBefore(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param T:
        :type T: Intrv_Interval &
        :rtype: None

        :param Index:
        :type Index: Standard_Integer
        :param S:
        :type S: Intrv_SequenceOfInterval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_InsertBefore(self, *args)

    def InsertAfter(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param T:
        :type T: Intrv_Interval &
        :rtype: None

        :param Index:
        :type Index: Standard_Integer
        :param S:
        :type S: Intrv_SequenceOfInterval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_InsertAfter(self, *args)

    def First(self):
        """
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_SequenceOfInterval_First(self)

    def Last(self):
        """
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_SequenceOfInterval_Last(self)

    def Split(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param Sub:
        :type Sub: Intrv_SequenceOfInterval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_Split(self, *args)

    def Value(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_SequenceOfInterval_Value(self, *args)

    def SetValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param I:
        :type I: Intrv_Interval &
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_SetValue(self, *args)

    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Intrv_Interval

        """
        return _Intrv.Intrv_SequenceOfInterval_ChangeValue(self, *args)

    def Remove(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: None

        :param FromIndex:
        :type FromIndex: Standard_Integer
        :param ToIndex:
        :type ToIndex: Standard_Integer
        :rtype: None

        """
        return _Intrv.Intrv_SequenceOfInterval_Remove(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


Intrv_SequenceOfInterval.Clear = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Clear,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Assign = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Assign,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Set = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Set,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Append = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Append,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Prepend = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Prepend,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.InsertBefore = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_InsertBefore,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.InsertAfter = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_InsertAfter,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.First = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_First,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Last = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Last,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Split = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Split,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Value = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Value,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.SetValue = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_SetValue,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.ChangeValue = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_ChangeValue,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval.Remove = new_instancemethod(_Intrv.Intrv_SequenceOfInterval_Remove,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval._kill_pointed = new_instancemethod(_Intrv.Intrv_SequenceOfInterval__kill_pointed,None,Intrv_SequenceOfInterval)
Intrv_SequenceOfInterval_swigregister = _Intrv.Intrv_SequenceOfInterval_swigregister
Intrv_SequenceOfInterval_swigregister(Intrv_SequenceOfInterval)



