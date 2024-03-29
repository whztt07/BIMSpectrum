# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _UnitsAPI.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_UnitsAPI', [dirname(__file__)])
        except ImportError:
            import _UnitsAPI
            return _UnitsAPI
        if fp is not None:
            try:
                _mod = imp.load_module('_UnitsAPI', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _UnitsAPI = swig_import_helper()
    del swig_import_helper
else:
    import _UnitsAPI
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
    __swig_destroy__ = _UnitsAPI.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_UnitsAPI.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_UnitsAPI.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_UnitsAPI.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_UnitsAPI.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_UnitsAPI.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_UnitsAPI.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_UnitsAPI.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_UnitsAPI.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_UnitsAPI.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_UnitsAPI.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_UnitsAPI.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_UnitsAPI.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_UnitsAPI.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_UnitsAPI.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_UnitsAPI.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_UnitsAPI.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _UnitsAPI.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.Units
import OCC.TCollection
import OCC.MMgt
import OCC.TColStd
UnitsAPI_DEFAULT = _UnitsAPI.UnitsAPI_DEFAULT
UnitsAPI_SI = _UnitsAPI.UnitsAPI_SI
UnitsAPI_MDTV = _UnitsAPI.UnitsAPI_MDTV
class unitsapi(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def CurrentToLS(*args):
        """
        * Converts the current unit value to the local system units value. Example: CurrentToLS(1.,'LENGTH') returns 1000. if the current length unit is meter and LocalSystem is MDTV.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentToLS(*args)

    CurrentToLS = staticmethod(CurrentToLS)
    def CurrentToSI(*args):
        """
        * Converts the current unit value to the SI system units value. Example: CurrentToSI(1.,'LENGTH') returns 0.001 if current length unit is millimeter.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentToSI(*args)

    CurrentToSI = staticmethod(CurrentToSI)
    def CurrentFromLS(*args):
        """
        * Converts the local system units value to the current unit value. Example: CurrentFromLS(1000.,'LENGTH') returns 1. if current length unit is meter and LocalSystem is MDTV.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentFromLS(*args)

    CurrentFromLS = staticmethod(CurrentFromLS)
    def CurrentFromSI(*args):
        """
        * Converts the SI system units value to the current unit value. Example: CurrentFromSI(0.001,'LENGTH') returns 1 if current length unit is millimeter.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentFromSI(*args)

    CurrentFromSI = staticmethod(CurrentFromSI)
    def AnyToLS(*args):
        """
        * Converts the local unit value to the local system units value. Example: AnyToLS(1.,'in.') returns 25.4 if the LocalSystem is MDTV.

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        * Converts the local unit value to the local system units value. and gives the associated dimension of the unit

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :param aDim:
        :type aDim: Handle_Units_Dimensions &
        :rtype: float

        """
        return _UnitsAPI.unitsapi_AnyToLS(*args)

    AnyToLS = staticmethod(AnyToLS)
    def AnyToSI(*args):
        """
        * Converts the local unit value to the SI system units value. Example: AnyToSI(1.,'in.') returns 0.0254

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        * Converts the local unit value to the SI system units value. and gives the associated dimension of the unit

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :param aDim:
        :type aDim: Handle_Units_Dimensions &
        :rtype: float

        """
        return _UnitsAPI.unitsapi_AnyToSI(*args)

    AnyToSI = staticmethod(AnyToSI)
    def AnyFromLS(*args):
        """
        * Converts the local system units value to the local unit value. Example: AnyFromLS(25.4,'in.') returns 1. if the LocalSystem is MDTV. Note: aUnit is also used to identify the type of physical quantity to convert.

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_AnyFromLS(*args)

    AnyFromLS = staticmethod(AnyFromLS)
    def AnyFromSI(*args):
        """
        * Converts the SI system units value to the local unit value. Example: AnyFromSI(0.0254,'in.') returns 0.001 Note: aUnit is also used to identify the type of physical quantity to convert.

        :param aData:
        :type aData: float
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_AnyFromSI(*args)

    AnyFromSI = staticmethod(AnyFromSI)
    def CurrentToAny(*args):
        """
        * Converts the aData value expressed in the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function, into the unit aUnit.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentToAny(*args)

    CurrentToAny = staticmethod(CurrentToAny)
    def CurrentFromAny(*args):
        """
        * Converts the aData value expressed in the unit aUnit, into the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :param aUnit:
        :type aUnit: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_CurrentFromAny(*args)

    CurrentFromAny = staticmethod(CurrentFromAny)
    def AnyToAny(*args):
        """
        * Converts the local unit value to another local unit value. Example: AnyToAny(0.0254,'in.','millimeter') returns 1. ;

        :param aData:
        :type aData: float
        :param aUnit1:
        :type aUnit1: char *
        :param aUnit2:
        :type aUnit2: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_AnyToAny(*args)

    AnyToAny = staticmethod(AnyToAny)
    def LSToSI(*args):
        """
        * Converts the local system units value to the SI system unit value. Example: LSToSI(1.,'LENGTH') returns 0.001 if the local system //!		length unit is millimeter.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_LSToSI(*args)

    LSToSI = staticmethod(LSToSI)
    def SIToLS(*args):
        """
        * Converts the SI system unit value to the local system units value. Example: SIToLS(1.,'LENGTH') returns 1000. if the local system //!		length unit is millimeter.

        :param aData:
        :type aData: float
        :param aQuantity:
        :type aQuantity: char *
        :rtype: float

        """
        return _UnitsAPI.unitsapi_SIToLS(*args)

    SIToLS = staticmethod(SIToLS)
    def SetLocalSystem(*args):
        """
        * Sets the local system units. Example: SetLocalSystem(UnitsAPI_MDTV)

        :param aSystemUnit: default value is UnitsAPI_SI
        :type aSystemUnit: UnitsAPI_SystemUnits
        :rtype: void

        * Sets the local system units. Example: SetLocalSystem(UnitsAPI_MDTV)

        :param aSystemUnit: default value is UnitsAPI_SI
        :type aSystemUnit: UnitsAPI_SystemUnits
        :rtype: void

        """
        return _UnitsAPI.unitsapi_SetLocalSystem(*args)

    SetLocalSystem = staticmethod(SetLocalSystem)
    def LocalSystem():
        """
        * Returns the current local system units.

        :rtype: UnitsAPI_SystemUnits

        """
        return _UnitsAPI.unitsapi_LocalSystem()

    LocalSystem = staticmethod(LocalSystem)
    def SetCurrentUnit(*args):
        """
        * Sets the current unit dimension <aUnit> to the unit quantity <aQuantity>. Example: SetCurrentUnit('LENGTH','millimeter')

        :param aQuantity:
        :type aQuantity: char *
        :param aUnit:
        :type aUnit: char *
        :rtype: void

        """
        return _UnitsAPI.unitsapi_SetCurrentUnit(*args)

    SetCurrentUnit = staticmethod(SetCurrentUnit)
    def CurrentUnit(*args):
        """
        * Returns the current unit dimension <aUnit> from the unit quantity <aQuantity>.

        :param aQuantity:
        :type aQuantity: char *
        :rtype: char *

        """
        return _UnitsAPI.unitsapi_CurrentUnit(*args)

    CurrentUnit = staticmethod(CurrentUnit)
    def Save():
        """
        * saves the units in the file .CurrentUnits of the directory pointed by the CSF_CurrentUnitsUserDefaults environment variable.

        :rtype: void

        """
        return _UnitsAPI.unitsapi_Save()

    Save = staticmethod(Save)
    def Reload():
        """
        :rtype: void

        """
        return _UnitsAPI.unitsapi_Reload()

    Reload = staticmethod(Reload)
    def Dimensions(*args):
        """
        * return the dimension associated to the quantity

        :param aQuantity:
        :type aQuantity: char *
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_Dimensions(*args)

    Dimensions = staticmethod(Dimensions)
    def DimensionLess():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionLess()

    DimensionLess = staticmethod(DimensionLess)
    def DimensionMass():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionMass()

    DimensionMass = staticmethod(DimensionMass)
    def DimensionLength():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionLength()

    DimensionLength = staticmethod(DimensionLength)
    def DimensionTime():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionTime()

    DimensionTime = staticmethod(DimensionTime)
    def DimensionElectricCurrent():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionElectricCurrent()

    DimensionElectricCurrent = staticmethod(DimensionElectricCurrent)
    def DimensionThermodynamicTemperature():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionThermodynamicTemperature()

    DimensionThermodynamicTemperature = staticmethod(DimensionThermodynamicTemperature)
    def DimensionAmountOfSubstance():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionAmountOfSubstance()

    DimensionAmountOfSubstance = staticmethod(DimensionAmountOfSubstance)
    def DimensionLuminousIntensity():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionLuminousIntensity()

    DimensionLuminousIntensity = staticmethod(DimensionLuminousIntensity)
    def DimensionPlaneAngle():
        """
        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionPlaneAngle()

    DimensionPlaneAngle = staticmethod(DimensionPlaneAngle)
    def DimensionSolidAngle():
        """
        * Returns the basic dimensions.

        :rtype: Handle_Units_Dimensions

        """
        return _UnitsAPI.unitsapi_DimensionSolidAngle()

    DimensionSolidAngle = staticmethod(DimensionSolidAngle)
    def Check(*args):
        """
        * Checks the coherence between the quantity <aQuantity> 	and the unit <aUnits> in the current system and //!		returns False when it's WRONG.

        :param aQuantity:
        :type aQuantity: char *
        :param aUnit:
        :type aUnit: char *
        :rtype: bool

        """
        return _UnitsAPI.unitsapi_Check(*args)

    Check = staticmethod(Check)
    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


unitsapi._kill_pointed = new_instancemethod(_UnitsAPI.unitsapi__kill_pointed,None,unitsapi)
unitsapi_swigregister = _UnitsAPI.unitsapi_swigregister
unitsapi_swigregister(unitsapi)

def unitsapi_CurrentToLS(*args):
  """
    * Converts the current unit value to the local system units value. Example: CurrentToLS(1.,'LENGTH') returns 1000. if the current length unit is meter and LocalSystem is MDTV.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentToLS(*args)

def unitsapi_CurrentToSI(*args):
  """
    * Converts the current unit value to the SI system units value. Example: CurrentToSI(1.,'LENGTH') returns 0.001 if current length unit is millimeter.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentToSI(*args)

def unitsapi_CurrentFromLS(*args):
  """
    * Converts the local system units value to the current unit value. Example: CurrentFromLS(1000.,'LENGTH') returns 1. if current length unit is meter and LocalSystem is MDTV.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentFromLS(*args)

def unitsapi_CurrentFromSI(*args):
  """
    * Converts the SI system units value to the current unit value. Example: CurrentFromSI(0.001,'LENGTH') returns 1 if current length unit is millimeter.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentFromSI(*args)

def unitsapi_AnyToLS(*args):
  """
    * Converts the local unit value to the local system units value. Example: AnyToLS(1.,'in.') returns 25.4 if the LocalSystem is MDTV.

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    * Converts the local unit value to the local system units value. and gives the associated dimension of the unit

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :param aDim:
    :type aDim: Handle_Units_Dimensions &
    :rtype: float

    """
  return _UnitsAPI.unitsapi_AnyToLS(*args)

def unitsapi_AnyToSI(*args):
  """
    * Converts the local unit value to the SI system units value. Example: AnyToSI(1.,'in.') returns 0.0254

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    * Converts the local unit value to the SI system units value. and gives the associated dimension of the unit

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :param aDim:
    :type aDim: Handle_Units_Dimensions &
    :rtype: float

    """
  return _UnitsAPI.unitsapi_AnyToSI(*args)

def unitsapi_AnyFromLS(*args):
  """
    * Converts the local system units value to the local unit value. Example: AnyFromLS(25.4,'in.') returns 1. if the LocalSystem is MDTV. Note: aUnit is also used to identify the type of physical quantity to convert.

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_AnyFromLS(*args)

def unitsapi_AnyFromSI(*args):
  """
    * Converts the SI system units value to the local unit value. Example: AnyFromSI(0.0254,'in.') returns 0.001 Note: aUnit is also used to identify the type of physical quantity to convert.

    :param aData:
    :type aData: float
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_AnyFromSI(*args)

def unitsapi_CurrentToAny(*args):
  """
    * Converts the aData value expressed in the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function, into the unit aUnit.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentToAny(*args)

def unitsapi_CurrentFromAny(*args):
  """
    * Converts the aData value expressed in the unit aUnit, into the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :param aUnit:
    :type aUnit: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_CurrentFromAny(*args)

def unitsapi_AnyToAny(*args):
  """
    * Converts the local unit value to another local unit value. Example: AnyToAny(0.0254,'in.','millimeter') returns 1. ;

    :param aData:
    :type aData: float
    :param aUnit1:
    :type aUnit1: char *
    :param aUnit2:
    :type aUnit2: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_AnyToAny(*args)

def unitsapi_LSToSI(*args):
  """
    * Converts the local system units value to the SI system unit value. Example: LSToSI(1.,'LENGTH') returns 0.001 if the local system //!		length unit is millimeter.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_LSToSI(*args)

def unitsapi_SIToLS(*args):
  """
    * Converts the SI system unit value to the local system units value. Example: SIToLS(1.,'LENGTH') returns 1000. if the local system //!		length unit is millimeter.

    :param aData:
    :type aData: float
    :param aQuantity:
    :type aQuantity: char *
    :rtype: float

    """
  return _UnitsAPI.unitsapi_SIToLS(*args)

def unitsapi_SetLocalSystem(*args):
  """
    * Sets the local system units. Example: SetLocalSystem(UnitsAPI_MDTV)

    :param aSystemUnit: default value is UnitsAPI_SI
    :type aSystemUnit: UnitsAPI_SystemUnits
    :rtype: void

    * Sets the local system units. Example: SetLocalSystem(UnitsAPI_MDTV)

    :param aSystemUnit: default value is UnitsAPI_SI
    :type aSystemUnit: UnitsAPI_SystemUnits
    :rtype: void

    """
  return _UnitsAPI.unitsapi_SetLocalSystem(*args)

def unitsapi_LocalSystem():
  """
    * Returns the current local system units.

    :rtype: UnitsAPI_SystemUnits

    """
  return _UnitsAPI.unitsapi_LocalSystem()

def unitsapi_SetCurrentUnit(*args):
  """
    * Sets the current unit dimension <aUnit> to the unit quantity <aQuantity>. Example: SetCurrentUnit('LENGTH','millimeter')

    :param aQuantity:
    :type aQuantity: char *
    :param aUnit:
    :type aUnit: char *
    :rtype: void

    """
  return _UnitsAPI.unitsapi_SetCurrentUnit(*args)

def unitsapi_CurrentUnit(*args):
  """
    * Returns the current unit dimension <aUnit> from the unit quantity <aQuantity>.

    :param aQuantity:
    :type aQuantity: char *
    :rtype: char *

    """
  return _UnitsAPI.unitsapi_CurrentUnit(*args)

def unitsapi_Save():
  """
    * saves the units in the file .CurrentUnits of the directory pointed by the CSF_CurrentUnitsUserDefaults environment variable.

    :rtype: void

    """
  return _UnitsAPI.unitsapi_Save()

def unitsapi_Reload():
  """
    :rtype: void

    """
  return _UnitsAPI.unitsapi_Reload()

def unitsapi_Dimensions(*args):
  """
    * return the dimension associated to the quantity

    :param aQuantity:
    :type aQuantity: char *
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_Dimensions(*args)

def unitsapi_DimensionLess():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionLess()

def unitsapi_DimensionMass():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionMass()

def unitsapi_DimensionLength():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionLength()

def unitsapi_DimensionTime():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionTime()

def unitsapi_DimensionElectricCurrent():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionElectricCurrent()

def unitsapi_DimensionThermodynamicTemperature():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionThermodynamicTemperature()

def unitsapi_DimensionAmountOfSubstance():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionAmountOfSubstance()

def unitsapi_DimensionLuminousIntensity():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionLuminousIntensity()

def unitsapi_DimensionPlaneAngle():
  """
    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionPlaneAngle()

def unitsapi_DimensionSolidAngle():
  """
    * Returns the basic dimensions.

    :rtype: Handle_Units_Dimensions

    """
  return _UnitsAPI.unitsapi_DimensionSolidAngle()

def unitsapi_Check(*args):
  """
    * Checks the coherence between the quantity <aQuantity> 	and the unit <aUnits> in the current system and //!		returns False when it's WRONG.

    :param aQuantity:
    :type aQuantity: char *
    :param aUnit:
    :type aUnit: char *
    :rtype: bool

    """
  return _UnitsAPI.unitsapi_Check(*args)



