# defining functions for use during my Physics class
import math

PI = math.pi
G = 9.81

def velocity1(d:float=None,t:float=None,v:float=None,verbose:bool=False):
    """Solves for the velocity formula "v = d/t". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        d (float, optional): Distance. Defaults to None.
        t (float, optional): Time. Defaults to None.
        v (float, optional): Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT. Defaults to False.

    Raises:
        ValueError: All Values Must be Numeric
        ValueError: There must be a single unknown value

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "v"

    try:
        d = float(d) if d is not None else None 
        t = float(t) if t is not None else None
        v = float(v) if v is not None else None
    except:
        raise ValueError("Non Numerics Passed as Values")
    
    if v is not None: 
        if d is None: 
            var = "d"
            result = v * t
        elif t is None:
            var = "t"
            result = d/v
        else: 
            raise ValueError("No Unknowns Passed")
    else: 
        result = d/t

    if verbose:
        print(f"velocity1: {var} = {result}")

    return result


def velocity2(vi:float=None,a:float=None,t:float=None,vf:float=None,verbose:bool=False):
    """Solves for the velocity formula "vf = vi + at". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        vi (float, optional): Initial Velocity. Defaults to None.
        a (float, optional): Acceleration. Defaults to None.
        t (float, optional): Time. Defaults to None.
        vf (float, optional): Final Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT. Defaults to False.

    Raises:
        ValueError: All Values Must be Numeric
        ValueError: There must be a single unknown value

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=None
    var = "vf" #used for verbose printing

    try: #converting from int to floats
        vi = float(vi) if vi is not None else None 
        a = float(a) if a is not None else None
        t = float(t) if t is not None else None
        vf = float(vf) if vf is not None else None
    except:
        raise ValueError("Non Numerics Passed as Values")
    
    if vf is not None: #if vf is not the variable being solved for
        if vi is None: #if we are solving for vi
            var = "vi"
            result = vf - (a * t)
        elif a is None: #if we are solving for a
            var = "a"
            result = (vf - vi) / t
        elif t is None: #if we are solving for t
            var = "t"
            result = (vf - vi) / a
        else: 
            raise ValueError("No Unknowns Passed")
    else: #if we are solving for vf
        result = vi + (a * t)
    
    #verbose acts as a switch thats prints the result to std out
    if verbose:
        print(f"velocity2: {var} = {result}")

    return result

if __name__ == "__main__":
    velocity1(
        d=20,
        t=5,
        verbose = True
    )

    velocity2(
        vi = 0,
        a = G,
        t = 3.4,
        verbose = True
        )