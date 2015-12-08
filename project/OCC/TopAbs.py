# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _TopAbs.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TopAbs', [dirname(__file__)])
        except ImportError:
            import _TopAbs
            return _TopAbs
        if fp is not None:
            try:
                _mod = imp.load_module('_TopAbs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TopAbs = swig_import_helper()
    del swig_import_helper
else:
    import _TopAbs
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
    __swig_destroy__ = _TopAbs.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_TopAbs.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_TopAbs.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_TopAbs.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_TopAbs.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_TopAbs.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_TopAbs.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_TopAbs.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_TopAbs.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_TopAbs.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_TopAbs.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_TopAbs.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_TopAbs.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_TopAbs.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_TopAbs.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_TopAbs.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_TopAbs.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _TopAbs.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
TopAbs_FORWARD = _TopAbs.TopAbs_FORWARD
TopAbs_REVERSED = _TopAbs.TopAbs_REVERSED
TopAbs_INTERNAL = _TopAbs.TopAbs_INTERNAL
TopAbs_EXTERNAL = _TopAbs.TopAbs_EXTERNAL
TopAbs_COMPOUND = _TopAbs.TopAbs_COMPOUND
TopAbs_COMPSOLID = _TopAbs.TopAbs_COMPSOLID
TopAbs_SOLID = _TopAbs.TopAbs_SOLID
TopAbs_SHELL = _TopAbs.TopAbs_SHELL
TopAbs_FACE = _TopAbs.TopAbs_FACE
TopAbs_WIRE = _TopAbs.TopAbs_WIRE
TopAbs_EDGE = _TopAbs.TopAbs_EDGE
TopAbs_VERTEX = _TopAbs.TopAbs_VERTEX
TopAbs_SHAPE = _TopAbs.TopAbs_SHAPE
TopAbs_IN = _TopAbs.TopAbs_IN
TopAbs_OUT = _TopAbs.TopAbs_OUT
TopAbs_ON = _TopAbs.TopAbs_ON
TopAbs_UNKNOWN = _TopAbs.TopAbs_UNKNOWN
class topabs(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def Compose(*args):
        """
        * Compose the Orientation <Or1> and <Or2>. This composition is not symmetric (if you switch <Or1> and <Or2> the result is different). It assumes that <Or1> is the Orientation of a Shape S1 containing a Shape S2 of Orientation Or2. The result is the cumulated orientation of S2 in S1. The composition law is :  \ Or2 FORWARD REVERSED INTERNAL EXTERNAL Or1 ------------------------------------- FORWARD | FORWARD REVERSED INTERNAL EXTERNAL  | REVERSED | REVERSED FORWARD INTERNAL EXTERNAL  | INTERNAL | INTERNAL INTERNAL INTERNAL INTERNAL  | EXTERNAL | EXTERNAL EXTERNAL EXTERNAL EXTERNAL Note: The top corner in the table is the most important for the purposes of Open CASCADE topology and shape sharing.

        :param Or1:
        :type Or1: TopAbs_Orientation
        :param Or2:
        :type Or2: TopAbs_Orientation
        :rtype: TopAbs_Orientation

        """
        return _TopAbs.topabs_Compose(*args)

    Compose = staticmethod(Compose)
    def Reverse(*args):
        """
        * xchanges the interior/exterior status of the two sides. This is what happens when the sense of direction is reversed. The following rules apply:  FORWARD REVERSED REVERSED FORWARD INTERNAL INTERNAL EXTERNAL EXTERNAL  Reverse exchange the material sides.

        :param Or:
        :type Or: TopAbs_Orientation
        :rtype: TopAbs_Orientation

        """
        return _TopAbs.topabs_Reverse(*args)

    Reverse = staticmethod(Reverse)
    def Complement(*args):
        """
        * Reverses the interior/exterior status of each side of the object. So, to take the complement of an object means to reverse the interior/exterior status of its boundary, i.e. inside becomes outside. The method returns the complementary orientation, following the rules in the table below: FORWARD REVERSED REVERSED FORWARD INTERNAL EXTERNAL EXTERNAL INTERNAL  Complement complements the material side. Inside becomes outside.

        :param Or:
        :type Or: TopAbs_Orientation
        :rtype: TopAbs_Orientation

        """
        return _TopAbs.topabs_Complement(*args)

    Complement = staticmethod(Complement)
    def Print(*args):
        """
        * Prints the name of Shape <SEq> as a String on the Stream <S> and returns <S>.

        :param SE:
        :type SE: TopAbs_ShapeEnum
        :param S:
        :type S: Standard_OStream &
        :rtype: Standard_OStream

        * Prints the name of the Orientation <Or> as a String on the Stream <S> and returns <S>.

        :param Or:
        :type Or: TopAbs_Orientation
        :param S:
        :type S: Standard_OStream &
        :rtype: Standard_OStream

        * Prints the name of the State <St> as a String on the Stream <S> and returns <S>.

        :param St:
        :type St: TopAbs_State
        :param S:
        :type S: Standard_OStream &
        :rtype: Standard_OStream

        """
        return _TopAbs.topabs_Print(*args)

    Print = staticmethod(Print)
    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


topabs._kill_pointed = new_instancemethod(_TopAbs.topabs__kill_pointed,None,topabs)
topabs_swigregister = _TopAbs.topabs_swigregister
topabs_swigregister(topabs)

def topabs_Compose(*args):
  """
    * Compose the Orientation <Or1> and <Or2>. This composition is not symmetric (if you switch <Or1> and <Or2> the result is different). It assumes that <Or1> is the Orientation of a Shape S1 containing a Shape S2 of Orientation Or2. The result is the cumulated orientation of S2 in S1. The composition law is :  \ Or2 FORWARD REVERSED INTERNAL EXTERNAL Or1 ------------------------------------- FORWARD | FORWARD REVERSED INTERNAL EXTERNAL  | REVERSED | REVERSED FORWARD INTERNAL EXTERNAL  | INTERNAL | INTERNAL INTERNAL INTERNAL INTERNAL  | EXTERNAL | EXTERNAL EXTERNAL EXTERNAL EXTERNAL Note: The top corner in the table is the most important for the purposes of Open CASCADE topology and shape sharing.

    :param Or1:
    :type Or1: TopAbs_Orientation
    :param Or2:
    :type Or2: TopAbs_Orientation
    :rtype: TopAbs_Orientation

    """
  return _TopAbs.topabs_Compose(*args)

def topabs_Reverse(*args):
  """
    * xchanges the interior/exterior status of the two sides. This is what happens when the sense of direction is reversed. The following rules apply:  FORWARD REVERSED REVERSED FORWARD INTERNAL INTERNAL EXTERNAL EXTERNAL  Reverse exchange the material sides.

    :param Or:
    :type Or: TopAbs_Orientation
    :rtype: TopAbs_Orientation

    """
  return _TopAbs.topabs_Reverse(*args)

def topabs_Complement(*args):
  """
    * Reverses the interior/exterior status of each side of the object. So, to take the complement of an object means to reverse the interior/exterior status of its boundary, i.e. inside becomes outside. The method returns the complementary orientation, following the rules in the table below: FORWARD REVERSED REVERSED FORWARD INTERNAL EXTERNAL EXTERNAL INTERNAL  Complement complements the material side. Inside becomes outside.

    :param Or:
    :type Or: TopAbs_Orientation
    :rtype: TopAbs_Orientation

    """
  return _TopAbs.topabs_Complement(*args)

def topabs_Print(*args):
  """
    * Prints the name of Shape <SEq> as a String on the Stream <S> and returns <S>.

    :param SE:
    :type SE: TopAbs_ShapeEnum
    :param S:
    :type S: Standard_OStream &
    :rtype: Standard_OStream

    * Prints the name of the Orientation <Or> as a String on the Stream <S> and returns <S>.

    :param Or:
    :type Or: TopAbs_Orientation
    :param S:
    :type S: Standard_OStream &
    :rtype: Standard_OStream

    * Prints the name of the State <St> as a String on the Stream <S> and returns <S>.

    :param St:
    :type St: TopAbs_State
    :param S:
    :type S: Standard_OStream &
    :rtype: Standard_OStream

    """
  return _TopAbs.topabs_Print(*args)



