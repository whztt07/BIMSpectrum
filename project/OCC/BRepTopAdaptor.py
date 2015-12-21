# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _BRepTopAdaptor.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BRepTopAdaptor', [dirname(__file__)])
        except ImportError:
            import _BRepTopAdaptor
            return _BRepTopAdaptor
        if fp is not None:
            try:
                _mod = imp.load_module('_BRepTopAdaptor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _BRepTopAdaptor = swig_import_helper()
    del swig_import_helper
else:
    import _BRepTopAdaptor
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
    __swig_destroy__ = _BRepTopAdaptor.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_BRepTopAdaptor.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_BRepTopAdaptor.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _BRepTopAdaptor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.TCollection
import OCC.Standard
import OCC.MMgt
import OCC.TopoDS
import OCC.TopLoc
import OCC.gp
import OCC.TopAbs
import OCC.Adaptor3d
import OCC.GeomAbs
import OCC.TColStd
import OCC.Geom
import OCC.TColgp
import OCC.Adaptor2d
import OCC.Geom2d
import OCC.math
import OCC.BRepAdaptor
import OCC.GeomAdaptor
import OCC.Geom2dAdaptor
class BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool(OCC.TCollection.TCollection_BasicMapIterator):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param aMap:
        :type aMap: BRepTopAdaptor_MapOfShapeTool &
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool(*args))
    def Initialize(self, *args):
        """
        :param aMap:
        :type aMap: BRepTopAdaptor_MapOfShapeTool &
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Initialize(self, *args)

    def Key(self):
        """
        :rtype: TopoDS_Shape

        """
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Key(self)

    def Value(self):
        """
        :rtype: BRepTopAdaptor_Tool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Value(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool.Initialize = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Initialize,None,BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool)
BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool.Key = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Key,None,BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool)
BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool.Value = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_Value,None,BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool)
BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool__kill_pointed,None,BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool)
BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_swigregister = _BRepTopAdaptor.BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_swigregister
BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool_swigregister(BRepTopAdaptor_DataMapIteratorOfMapOfShapeTool)

class BRepTopAdaptor_DataMapNodeOfMapOfShapeTool(OCC.TCollection.TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param K:
        :type K: TopoDS_Shape &
        :param I:
        :type I: BRepTopAdaptor_Tool &
        :param n:
        :type n: TCollection_MapNodePtr &
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool(*args))
    def Key(self):
        """
        :rtype: TopoDS_Shape

        """
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_Key(self)

    def Value(self):
        """
        :rtype: BRepTopAdaptor_Tool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_Value(self)

    def _kill_pointed(self):
        """_kill_pointed(BRepTopAdaptor_DataMapNodeOfMapOfShapeTool self)"""
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(BRepTopAdaptor_DataMapNodeOfMapOfShapeTool self) -> Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool"""
        return _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.Key = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_Key,None,BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.Value = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_Value,None,BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
BRepTopAdaptor_DataMapNodeOfMapOfShapeTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool__kill_pointed,None,BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.GetHandle = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_GetHandle,None,BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister = _BRepTopAdaptor.BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister
BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister(BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)

class Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool(OCC.TCollection.Handle_TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swiginit(self,_BRepTopAdaptor.new_Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool(*args))
    DownCast = staticmethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.Nullify = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_Nullify,None,Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.IsNull = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_IsNull,None,Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool.GetObject = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_GetObject,None,Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool__kill_pointed,None,Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister = _BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_swigregister(Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool)

def Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_DownCast(*args):
  return _BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_DownCast(*args)
Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_DownCast = _BRepTopAdaptor.Handle_BRepTopAdaptor_DataMapNodeOfMapOfShapeTool_DownCast

class BRepTopAdaptor_FClass2d(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param F:
        :type F: TopoDS_Face &
        :param Tol:
        :type Tol: float
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_FClass2d_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_FClass2d(*args))
    def PerformInfinitePoint(self):
        """
        :rtype: TopAbs_State

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_PerformInfinitePoint(self)

    def Perform(self, *args):
        """
        :param Puv:
        :type Puv: gp_Pnt2d
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        :param Puv:
        :type Puv: gp_Pnt2d
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_Perform(self, *args)

    def Destroy(self):
        """
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_Destroy(self)

    def Copy(self, *args):
        """
        :param Other:
        :type Other: BRepTopAdaptor_FClass2d &
        :rtype: BRepTopAdaptor_FClass2d

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_Copy(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: BRepTopAdaptor_FClass2d &
        :rtype: BRepTopAdaptor_FClass2d

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_Set(self, *args)

    def TestOnRestriction(self, *args):
        """
        * Test a point with +- an offset (Tol) and returns On if some points are OUT an some are IN (Caution: Internal use . see the code for more details)

        :param Puv:
        :type Puv: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        * Test a point with +- an offset (Tol) and returns On if some points are OUT an some are IN (Caution: Internal use . see the code for more details)

        :param Puv:
        :type Puv: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        """
        return _BRepTopAdaptor.BRepTopAdaptor_FClass2d_TestOnRestriction(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_FClass2d.PerformInfinitePoint = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_PerformInfinitePoint,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d.Perform = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Perform,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d.Destroy = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Destroy,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d.Copy = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Copy,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d.Set = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_Set,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d.TestOnRestriction = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d_TestOnRestriction,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_FClass2d__kill_pointed,None,BRepTopAdaptor_FClass2d)
BRepTopAdaptor_FClass2d_swigregister = _BRepTopAdaptor.BRepTopAdaptor_FClass2d_swigregister
BRepTopAdaptor_FClass2d_swigregister(BRepTopAdaptor_FClass2d)

class BRepTopAdaptor_HVertex(OCC.Adaptor3d.Adaptor3d_HVertex):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param Vtx:
        :type Vtx: TopoDS_Vertex &
        :param Curve:
        :type Curve: Handle_BRepAdaptor_HCurve2d &
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_HVertex_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_HVertex(*args))
    def Vertex(self):
        """
        :rtype: TopoDS_Vertex

        """
        return _BRepTopAdaptor.BRepTopAdaptor_HVertex_Vertex(self)

    def ChangeVertex(self):
        """
        :rtype: TopoDS_Vertex

        """
        return _BRepTopAdaptor.BRepTopAdaptor_HVertex_ChangeVertex(self)

    def _kill_pointed(self):
        """_kill_pointed(BRepTopAdaptor_HVertex self)"""
        return _BRepTopAdaptor.BRepTopAdaptor_HVertex__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(BRepTopAdaptor_HVertex self) -> Handle_BRepTopAdaptor_HVertex"""
        return _BRepTopAdaptor.BRepTopAdaptor_HVertex_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_HVertex.Vertex = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_HVertex_Vertex,None,BRepTopAdaptor_HVertex)
BRepTopAdaptor_HVertex.ChangeVertex = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_HVertex_ChangeVertex,None,BRepTopAdaptor_HVertex)
BRepTopAdaptor_HVertex._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_HVertex__kill_pointed,None,BRepTopAdaptor_HVertex)
BRepTopAdaptor_HVertex.GetHandle = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_HVertex_GetHandle,None,BRepTopAdaptor_HVertex)
BRepTopAdaptor_HVertex_swigregister = _BRepTopAdaptor.BRepTopAdaptor_HVertex_swigregister
BRepTopAdaptor_HVertex_swigregister(BRepTopAdaptor_HVertex)

class Handle_BRepTopAdaptor_HVertex(OCC.Adaptor3d.Handle_Adaptor3d_HVertex):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_swiginit(self,_BRepTopAdaptor.new_Handle_BRepTopAdaptor_HVertex(*args))
    DownCast = staticmethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_BRepTopAdaptor_HVertex.Nullify = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_Nullify,None,Handle_BRepTopAdaptor_HVertex)
Handle_BRepTopAdaptor_HVertex.IsNull = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_IsNull,None,Handle_BRepTopAdaptor_HVertex)
Handle_BRepTopAdaptor_HVertex.GetObject = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_GetObject,None,Handle_BRepTopAdaptor_HVertex)
Handle_BRepTopAdaptor_HVertex._kill_pointed = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex__kill_pointed,None,Handle_BRepTopAdaptor_HVertex)
Handle_BRepTopAdaptor_HVertex_swigregister = _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_swigregister
Handle_BRepTopAdaptor_HVertex_swigregister(Handle_BRepTopAdaptor_HVertex)

def Handle_BRepTopAdaptor_HVertex_DownCast(*args):
  return _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_DownCast(*args)
Handle_BRepTopAdaptor_HVertex_DownCast = _BRepTopAdaptor.Handle_BRepTopAdaptor_HVertex_DownCast

class BRepTopAdaptor_MapOfShapeTool(OCC.TCollection.TCollection_BasicMap):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, NbBuckets=1): 
        """
        :param NbBuckets: default value is 1
        :type NbBuckets: Standard_Integer
        :rtype: None

        :param NbBuckets: default value is 1
        :type NbBuckets: Standard_Integer
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_MapOfShapeTool(NbBuckets))
    def Assign(self, *args):
        """
        :param Other:
        :type Other: BRepTopAdaptor_MapOfShapeTool &
        :rtype: BRepTopAdaptor_MapOfShapeTool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: BRepTopAdaptor_MapOfShapeTool &
        :rtype: BRepTopAdaptor_MapOfShapeTool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Set(self, *args)

    def ReSize(self, *args):
        """
        :param NbBuckets:
        :type NbBuckets: Standard_Integer
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ReSize(self, *args)

    def Clear(self):
        """
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Clear(self)

    def Bind(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :param I:
        :type I: BRepTopAdaptor_Tool &
        :rtype: bool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Bind(self, *args)

    def IsBound(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: bool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_IsBound(self, *args)

    def UnBind(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: bool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_UnBind(self, *args)

    def Find(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: BRepTopAdaptor_Tool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Find(self, *args)

    def ChangeFind(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: BRepTopAdaptor_Tool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeFind(self, *args)

    def Find1(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: Standard_Address

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Find1(self, *args)

    def ChangeFind1(self, *args):
        """
        :param K:
        :type K: TopoDS_Shape &
        :rtype: Standard_Address

        """
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeFind1(self, *args)

    def _kill_pointed(self):
        """_kill_pointed(BRepTopAdaptor_MapOfShapeTool self)"""
        return _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool__kill_pointed(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_MapOfShapeTool.Assign = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Assign,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.Set = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Set,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.ReSize = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ReSize,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.Clear = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Clear,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.Bind = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Bind,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.IsBound = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_IsBound,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.UnBind = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_UnBind,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.Find = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Find,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.ChangeFind = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeFind,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.Find1 = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_Find1,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool.ChangeFind1 = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_ChangeFind1,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool__kill_pointed,None,BRepTopAdaptor_MapOfShapeTool)
BRepTopAdaptor_MapOfShapeTool_swigregister = _BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool_swigregister
BRepTopAdaptor_MapOfShapeTool_swigregister(BRepTopAdaptor_MapOfShapeTool)

class BRepTopAdaptor_Tool(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param F:
        :type F: TopoDS_Face &
        :param Tol2d:
        :type Tol2d: float
        :rtype: None

        :param Surface:
        :type Surface: Handle_Adaptor3d_HSurface &
        :param Tol2d:
        :type Tol2d: float
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_Tool_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_Tool(*args))
    def Init(self, *args):
        """
        :param F:
        :type F: TopoDS_Face &
        :param Tol2d:
        :type Tol2d: float
        :rtype: None

        :param Surface:
        :type Surface: Handle_Adaptor3d_HSurface &
        :param Tol2d:
        :type Tol2d: float
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_Tool_Init(self, *args)

    def GetTopolTool(self):
        """
        :rtype: Handle_BRepTopAdaptor_TopolTool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_Tool_GetTopolTool(self)

    def SetTopolTool(self, *args):
        """
        :param TT:
        :type TT: Handle_BRepTopAdaptor_TopolTool &
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_Tool_SetTopolTool(self, *args)

    def GetSurface(self):
        """
        :rtype: Handle_Adaptor3d_HSurface

        """
        return _BRepTopAdaptor.BRepTopAdaptor_Tool_GetSurface(self)

    def Destroy(self):
        """
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_Tool_Destroy(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_Tool.Init = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool_Init,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool.GetTopolTool = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool_GetTopolTool,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool.SetTopolTool = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool_SetTopolTool,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool.GetSurface = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool_GetSurface,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool.Destroy = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool_Destroy,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_Tool__kill_pointed,None,BRepTopAdaptor_Tool)
BRepTopAdaptor_Tool_swigregister = _BRepTopAdaptor.BRepTopAdaptor_Tool_swigregister
BRepTopAdaptor_Tool_swigregister(BRepTopAdaptor_Tool)

class BRepTopAdaptor_TopolTool(OCC.Adaptor3d.Adaptor3d_TopolTool):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param Surface:
        :type Surface: Handle_Adaptor3d_HSurface &
        :rtype: None

        """
        _BRepTopAdaptor.BRepTopAdaptor_TopolTool_swiginit(self,_BRepTopAdaptor.new_BRepTopAdaptor_TopolTool(*args))
    def Initialize(self, *args):
        """
        :rtype: void

        :param S:
        :type S: Handle_Adaptor3d_HSurface &
        :rtype: void

        :param Curve:
        :type Curve: Handle_Adaptor2d_HCurve2d &
        :rtype: void

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_Initialize(self, *args)

    def Classify(self, *args):
        """
        :param P2d:
        :type P2d: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        :param P2d:
        :type P2d: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: TopAbs_State

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_Classify(self, *args)

    def IsThePointOn(self, *args):
        """
        * see the code for specifications)

        :param P2d:
        :type P2d: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: bool

        * see the code for specifications)

        :param P2d:
        :type P2d: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :param RecadreOnPeriodic: default value is Standard_True
        :type RecadreOnPeriodic: bool
        :rtype: bool

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_IsThePointOn(self, *args)

    def Orientation(self, *args):
        """
        * If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a 'real' limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.

        :param C:
        :type C: Handle_Adaptor2d_HCurve2d &
        :rtype: TopAbs_Orientation

        * If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a 'real' limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.

        :param C:
        :type C: Handle_Adaptor3d_HVertex &
        :rtype: TopAbs_Orientation

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_Orientation(self, *args)

    def Destroy(self):
        """
        :rtype: None

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_Destroy(self)

    def Tol3d(self, *args):
        """
        * returns 3d tolerance of the arc C

        :param C:
        :type C: Handle_Adaptor2d_HCurve2d &
        :rtype: float

        * returns 3d tolerance of the vertex V

        :param V:
        :type V: Handle_Adaptor3d_HVertex &
        :rtype: float

        """
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_Tol3d(self, *args)

    def _kill_pointed(self):
        """_kill_pointed(BRepTopAdaptor_TopolTool self)"""
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(BRepTopAdaptor_TopolTool self) -> Handle_BRepTopAdaptor_TopolTool"""
        return _BRepTopAdaptor.BRepTopAdaptor_TopolTool_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


BRepTopAdaptor_TopolTool.Initialize = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Initialize,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.Classify = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Classify,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.IsThePointOn = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_IsThePointOn,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.Orientation = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Orientation,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.Destroy = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Destroy,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.Tol3d = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_Tol3d,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool__kill_pointed,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool.GetHandle = new_instancemethod(_BRepTopAdaptor.BRepTopAdaptor_TopolTool_GetHandle,None,BRepTopAdaptor_TopolTool)
BRepTopAdaptor_TopolTool_swigregister = _BRepTopAdaptor.BRepTopAdaptor_TopolTool_swigregister
BRepTopAdaptor_TopolTool_swigregister(BRepTopAdaptor_TopolTool)

class Handle_BRepTopAdaptor_TopolTool(OCC.Adaptor3d.Handle_Adaptor3d_TopolTool):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_swiginit(self,_BRepTopAdaptor.new_Handle_BRepTopAdaptor_TopolTool(*args))
    DownCast = staticmethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_BRepTopAdaptor_TopolTool.Nullify = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_Nullify,None,Handle_BRepTopAdaptor_TopolTool)
Handle_BRepTopAdaptor_TopolTool.IsNull = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_IsNull,None,Handle_BRepTopAdaptor_TopolTool)
Handle_BRepTopAdaptor_TopolTool.GetObject = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_GetObject,None,Handle_BRepTopAdaptor_TopolTool)
Handle_BRepTopAdaptor_TopolTool._kill_pointed = new_instancemethod(_BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool__kill_pointed,None,Handle_BRepTopAdaptor_TopolTool)
Handle_BRepTopAdaptor_TopolTool_swigregister = _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_swigregister
Handle_BRepTopAdaptor_TopolTool_swigregister(Handle_BRepTopAdaptor_TopolTool)

def Handle_BRepTopAdaptor_TopolTool_DownCast(*args):
  return _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_DownCast(*args)
Handle_BRepTopAdaptor_TopolTool_DownCast = _BRepTopAdaptor.Handle_BRepTopAdaptor_TopolTool_DownCast


