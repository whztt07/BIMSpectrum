# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _TColQuantity.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TColQuantity', [dirname(__file__)])
        except ImportError:
            import _TColQuantity
            return _TColQuantity
        if fp is not None:
            try:
                _mod = imp.load_module('_TColQuantity', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TColQuantity = swig_import_helper()
    del swig_import_helper
else:
    import _TColQuantity
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
    __swig_destroy__ = _TColQuantity.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_TColQuantity.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_TColQuantity.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_TColQuantity.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_TColQuantity.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_TColQuantity.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_TColQuantity.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_TColQuantity.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_TColQuantity.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_TColQuantity.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_TColQuantity.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_TColQuantity.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_TColQuantity.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_TColQuantity.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_TColQuantity.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_TColQuantity.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_TColQuantity.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _TColQuantity.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.Quantity
import OCC.TCollection
import OCC.MMgt
class TColQuantity_Array1OfLength(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param Low:
        :type Low: Standard_Integer
        :param Up:
        :type Up: Standard_Integer
        :rtype: None

        :param Item:
        :type Item: Quantity_Length &
        :param Low:
        :type Low: Standard_Integer
        :param Up:
        :type Up: Standard_Integer
        :rtype: None

        """
        _TColQuantity.TColQuantity_Array1OfLength_swiginit(self,_TColQuantity.new_TColQuantity_Array1OfLength(*args))
    def Init(self, *args):
        """
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Init(self, *args)

    def Destroy(self):
        """
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Destroy(self)

    def IsAllocated(self):
        """
        :rtype: bool

        """
        return _TColQuantity.TColQuantity_Array1OfLength_IsAllocated(self)

    def Assign(self, *args):
        """
        :param Other:
        :type Other: TColQuantity_Array1OfLength &
        :rtype: TColQuantity_Array1OfLength

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: TColQuantity_Array1OfLength &
        :rtype: TColQuantity_Array1OfLength

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Set(self, *args)

    def Length(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Length(self)

    def Lower(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Lower(self)

    def Upper(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Upper(self)

    def SetValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param Value:
        :type Value: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array1OfLength_SetValue(self, *args)

    def Value(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_Array1OfLength_Value(self, *args)

    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_Array1OfLength_ChangeValue(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


TColQuantity_Array1OfLength.Init = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Init,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Destroy = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Destroy,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.IsAllocated = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_IsAllocated,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Assign = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Assign,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Set = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Set,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Length = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Length,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Lower = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Lower,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Upper = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Upper,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.SetValue = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_SetValue,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.Value = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_Value,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength.ChangeValue = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength_ChangeValue,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength._kill_pointed = new_instancemethod(_TColQuantity.TColQuantity_Array1OfLength__kill_pointed,None,TColQuantity_Array1OfLength)
TColQuantity_Array1OfLength_swigregister = _TColQuantity.TColQuantity_Array1OfLength_swigregister
TColQuantity_Array1OfLength_swigregister(TColQuantity_Array1OfLength)

class TColQuantity_Array2OfLength(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param R1:
        :type R1: Standard_Integer
        :param R2:
        :type R2: Standard_Integer
        :param C1:
        :type C1: Standard_Integer
        :param C2:
        :type C2: Standard_Integer
        :rtype: None

        :param Item:
        :type Item: Quantity_Length &
        :param R1:
        :type R1: Standard_Integer
        :param R2:
        :type R2: Standard_Integer
        :param C1:
        :type C1: Standard_Integer
        :param C2:
        :type C2: Standard_Integer
        :rtype: None

        """
        _TColQuantity.TColQuantity_Array2OfLength_swiginit(self,_TColQuantity.new_TColQuantity_Array2OfLength(*args))
    def Init(self, *args):
        """
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array2OfLength_Init(self, *args)

    def Destroy(self):
        """
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array2OfLength_Destroy(self)

    def Assign(self, *args):
        """
        :param Other:
        :type Other: TColQuantity_Array2OfLength &
        :rtype: TColQuantity_Array2OfLength

        """
        return _TColQuantity.TColQuantity_Array2OfLength_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: TColQuantity_Array2OfLength &
        :rtype: TColQuantity_Array2OfLength

        """
        return _TColQuantity.TColQuantity_Array2OfLength_Set(self, *args)

    def ColLength(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_ColLength(self)

    def RowLength(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_RowLength(self)

    def LowerCol(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_LowerCol(self)

    def LowerRow(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_LowerRow(self)

    def UpperCol(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_UpperCol(self)

    def UpperRow(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_Array2OfLength_UpperRow(self)

    def SetValue(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :param Value:
        :type Value: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_Array2OfLength_SetValue(self, *args)

    def Value(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_Array2OfLength_Value(self, *args)

    def ChangeValue(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_Array2OfLength_ChangeValue(self, *args)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


TColQuantity_Array2OfLength.Init = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_Init,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.Destroy = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_Destroy,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.Assign = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_Assign,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.Set = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_Set,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.ColLength = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_ColLength,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.RowLength = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_RowLength,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.LowerCol = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_LowerCol,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.LowerRow = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_LowerRow,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.UpperCol = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_UpperCol,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.UpperRow = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_UpperRow,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.SetValue = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_SetValue,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.Value = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_Value,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength.ChangeValue = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength_ChangeValue,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength._kill_pointed = new_instancemethod(_TColQuantity.TColQuantity_Array2OfLength__kill_pointed,None,TColQuantity_Array2OfLength)
TColQuantity_Array2OfLength_swigregister = _TColQuantity.TColQuantity_Array2OfLength_swigregister
TColQuantity_Array2OfLength_swigregister(TColQuantity_Array2OfLength)

class TColQuantity_HArray1OfLength(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param Low:
        :type Low: Standard_Integer
        :param Up:
        :type Up: Standard_Integer
        :rtype: None

        :param Low:
        :type Low: Standard_Integer
        :param Up:
        :type Up: Standard_Integer
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        _TColQuantity.TColQuantity_HArray1OfLength_swiginit(self,_TColQuantity.new_TColQuantity_HArray1OfLength(*args))
    def Init(self, *args):
        """
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Init(self, *args)

    def Length(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Length(self)

    def Lower(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Lower(self)

    def Upper(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Upper(self)

    def SetValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :param Value:
        :type Value: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_SetValue(self, *args)

    def Value(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Value(self, *args)

    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_ChangeValue(self, *args)

    def Array1(self):
        """
        :rtype: TColQuantity_Array1OfLength

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_Array1(self)

    def ChangeArray1(self):
        """
        :rtype: TColQuantity_Array1OfLength

        """
        return _TColQuantity.TColQuantity_HArray1OfLength_ChangeArray1(self)

    def _kill_pointed(self):
        """_kill_pointed(TColQuantity_HArray1OfLength self)"""
        return _TColQuantity.TColQuantity_HArray1OfLength__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(TColQuantity_HArray1OfLength self) -> Handle_TColQuantity_HArray1OfLength"""
        return _TColQuantity.TColQuantity_HArray1OfLength_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


TColQuantity_HArray1OfLength.Init = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Init,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.Length = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Length,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.Lower = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Lower,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.Upper = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Upper,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.SetValue = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_SetValue,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.Value = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Value,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.ChangeValue = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_ChangeValue,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.Array1 = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_Array1,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.ChangeArray1 = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_ChangeArray1,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength._kill_pointed = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength__kill_pointed,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength.GetHandle = new_instancemethod(_TColQuantity.TColQuantity_HArray1OfLength_GetHandle,None,TColQuantity_HArray1OfLength)
TColQuantity_HArray1OfLength_swigregister = _TColQuantity.TColQuantity_HArray1OfLength_swigregister
TColQuantity_HArray1OfLength_swigregister(TColQuantity_HArray1OfLength)

class Handle_TColQuantity_HArray1OfLength(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _TColQuantity.Handle_TColQuantity_HArray1OfLength_swiginit(self,_TColQuantity.new_Handle_TColQuantity_HArray1OfLength(*args))
    DownCast = staticmethod(_TColQuantity.Handle_TColQuantity_HArray1OfLength_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_TColQuantity_HArray1OfLength.Nullify = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray1OfLength_Nullify,None,Handle_TColQuantity_HArray1OfLength)
Handle_TColQuantity_HArray1OfLength.IsNull = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray1OfLength_IsNull,None,Handle_TColQuantity_HArray1OfLength)
Handle_TColQuantity_HArray1OfLength.GetObject = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray1OfLength_GetObject,None,Handle_TColQuantity_HArray1OfLength)
Handle_TColQuantity_HArray1OfLength._kill_pointed = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray1OfLength__kill_pointed,None,Handle_TColQuantity_HArray1OfLength)
Handle_TColQuantity_HArray1OfLength_swigregister = _TColQuantity.Handle_TColQuantity_HArray1OfLength_swigregister
Handle_TColQuantity_HArray1OfLength_swigregister(Handle_TColQuantity_HArray1OfLength)

def Handle_TColQuantity_HArray1OfLength_DownCast(*args):
  return _TColQuantity.Handle_TColQuantity_HArray1OfLength_DownCast(*args)
Handle_TColQuantity_HArray1OfLength_DownCast = _TColQuantity.Handle_TColQuantity_HArray1OfLength_DownCast

class TColQuantity_HArray2OfLength(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param R1:
        :type R1: Standard_Integer
        :param R2:
        :type R2: Standard_Integer
        :param C1:
        :type C1: Standard_Integer
        :param C2:
        :type C2: Standard_Integer
        :rtype: None

        :param R1:
        :type R1: Standard_Integer
        :param R2:
        :type R2: Standard_Integer
        :param C1:
        :type C1: Standard_Integer
        :param C2:
        :type C2: Standard_Integer
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        _TColQuantity.TColQuantity_HArray2OfLength_swiginit(self,_TColQuantity.new_TColQuantity_HArray2OfLength(*args))
    def Init(self, *args):
        """
        :param V:
        :type V: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_Init(self, *args)

    def ColLength(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_ColLength(self)

    def RowLength(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_RowLength(self)

    def LowerCol(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_LowerCol(self)

    def LowerRow(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_LowerRow(self)

    def UpperCol(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_UpperCol(self)

    def UpperRow(self):
        """
        :rtype: int

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_UpperRow(self)

    def SetValue(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :param Value:
        :type Value: Quantity_Length &
        :rtype: None

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_SetValue(self, *args)

    def Value(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_Value(self, *args)

    def ChangeValue(self, *args):
        """
        :param Row:
        :type Row: Standard_Integer
        :param Col:
        :type Col: Standard_Integer
        :rtype: Quantity_Length

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_ChangeValue(self, *args)

    def Array2(self):
        """
        :rtype: TColQuantity_Array2OfLength

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_Array2(self)

    def ChangeArray2(self):
        """
        :rtype: TColQuantity_Array2OfLength

        """
        return _TColQuantity.TColQuantity_HArray2OfLength_ChangeArray2(self)

    def _kill_pointed(self):
        """_kill_pointed(TColQuantity_HArray2OfLength self)"""
        return _TColQuantity.TColQuantity_HArray2OfLength__kill_pointed(self)

    def GetHandle(self):
        """GetHandle(TColQuantity_HArray2OfLength self) -> Handle_TColQuantity_HArray2OfLength"""
        return _TColQuantity.TColQuantity_HArray2OfLength_GetHandle(self)

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


TColQuantity_HArray2OfLength.Init = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_Init,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.ColLength = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_ColLength,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.RowLength = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_RowLength,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.LowerCol = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_LowerCol,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.LowerRow = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_LowerRow,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.UpperCol = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_UpperCol,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.UpperRow = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_UpperRow,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.SetValue = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_SetValue,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.Value = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_Value,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.ChangeValue = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_ChangeValue,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.Array2 = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_Array2,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.ChangeArray2 = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_ChangeArray2,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength._kill_pointed = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength__kill_pointed,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength.GetHandle = new_instancemethod(_TColQuantity.TColQuantity_HArray2OfLength_GetHandle,None,TColQuantity_HArray2OfLength)
TColQuantity_HArray2OfLength_swigregister = _TColQuantity.TColQuantity_HArray2OfLength_swigregister
TColQuantity_HArray2OfLength_swigregister(TColQuantity_HArray2OfLength)

class Handle_TColQuantity_HArray2OfLength(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _TColQuantity.Handle_TColQuantity_HArray2OfLength_swiginit(self,_TColQuantity.new_Handle_TColQuantity_HArray2OfLength(*args))
    DownCast = staticmethod(_TColQuantity.Handle_TColQuantity_HArray2OfLength_DownCast)
    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_TColQuantity_HArray2OfLength.Nullify = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray2OfLength_Nullify,None,Handle_TColQuantity_HArray2OfLength)
Handle_TColQuantity_HArray2OfLength.IsNull = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray2OfLength_IsNull,None,Handle_TColQuantity_HArray2OfLength)
Handle_TColQuantity_HArray2OfLength.GetObject = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray2OfLength_GetObject,None,Handle_TColQuantity_HArray2OfLength)
Handle_TColQuantity_HArray2OfLength._kill_pointed = new_instancemethod(_TColQuantity.Handle_TColQuantity_HArray2OfLength__kill_pointed,None,Handle_TColQuantity_HArray2OfLength)
Handle_TColQuantity_HArray2OfLength_swigregister = _TColQuantity.Handle_TColQuantity_HArray2OfLength_swigregister
Handle_TColQuantity_HArray2OfLength_swigregister(Handle_TColQuantity_HArray2OfLength)

def Handle_TColQuantity_HArray2OfLength_DownCast(*args):
  return _TColQuantity.Handle_TColQuantity_HArray2OfLength_DownCast(*args)
Handle_TColQuantity_HArray2OfLength_DownCast = _TColQuantity.Handle_TColQuantity_HArray2OfLength_DownCast



