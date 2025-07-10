# defining functions for use during my Physics class
# all code written by joegriffin2000
import math

PI = math.pi
G = 9.81

def velocity1(d:float=None,t:float=None,v:float=None,verbose:bool=False) -> float:
    """Solves for the velocity formula "v = d/t". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        d (float, optional): Distance. Defaults to None.
        t (float, optional): Time. Defaults to None.
        v (float, optional): Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT. Defaults to False.

    Raises:
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

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
        raise ValueError(f"Non Numerics Passed as Values (d,t,v):({d},{t},{v})") if verbose else ValueError("Non Numerics Passed as Values")
    
    if v is not None: 
        if d is None: 
            var = "d"
            result = v * t
        elif t is None:
            var = "t"
            result = d/v
        else: 
            raise ValueError(f"No Unknowns Passed (d,t,v):({d},{t},{v})") if verbose else ValueError("No Unknowns Passed")
    else:
        if d is None or t is None:
            raise ValueError(f"Too Many Unknowns (d,t,v):({d},{t},{v})") if verbose else ValueError("Too Many Unknowns")
        result = d/t

    if verbose:
        print(f"velocity1: {var} = {result}")

    return result


def velocity2(vi:float=None,a:float=None,t:float=None,vf:float=None,verbose:bool=False)-> float:
    """Solves for the velocity formula "vf = vi + at". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        vi (float, optional): Initial Velocity. Defaults to None.
        a (float, optional): Acceleration. Defaults to None.
        t (float, optional): Time. Defaults to None.
        vf (float, optional): Final Velocity. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.

    Raises:
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

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
        raise ValueError(f"Non Numerics Passed as Values (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("Non Numerics Passed as Values")
    
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
            raise ValueError(f"No Unknowns Passed (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("No Unknowns Passed")
    else: #if we are solving for vf
        if vi is None or a is None or t is None:
            raise ValueError(f"Too Many Unknowns (vi,a,t,vf):({vi},{a},{t},{vf})") if verbose else ValueError("Too Many Unknowns")
        result = vi + (a * t)
    
    #verbose acts as a switch thats prints the result to std out
    if verbose:
        print(f"velocity2: {var} = {result}")

    return result

def velocity_vector(i:float=None,j:float=None,r:float=None,verbose:bool=False)-> float:
    """Solves for the vector formula "vr^2 = vi^2 + vj^2". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        i (float, optional): Vector i Component. Defaults to None.
        j (float, optional): Vector j Component. Defaults to None.
        r (float, optional): Result Vector Magnitude. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.

    Raises:
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "r"

    try:
        i = float(i) if i is not None else None 
        j = float(j) if j is not None else None
        r = float(r) if r is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (i,j,r):({i},{j},{r})") if verbose else ValueError("Non Numerics Passed as Values")
    
    if r is not None: 
        if i is None: 
            var = "i"
            result = math.sqrt(r**2 - j**2)
        elif j is None:
            var = "j"
            result = math.sqrt(r**2 - i**2)
        else: 
            raise ValueError(f"No Unknowns Passed (i,j,r):({i},{j},{r})") if verbose else ValueError("No Unknowns Passed")
    else: 
        if j is None or i is None:
            raise ValueError(f"Too Many Unknowns (i,j,r):({i},{j},{r})") if verbose else ValueError("Too Many Unknowns")
        result = math.sqrt(i**2 + j**2)

    if verbose:
        print(f"velocity_vector: {var} = {result}")

    return result

def displacement(vi:float=None,t:float=None,a:float=None,x:float=None,verbose:bool=False)-> float:
    """Solves for the displacement formula "x = vi*t + 1/2*a*t^2". All values are assumed to be converted to the right units prior to function. Only one unknown allowed per call.

    Args:
        vi (float, optional): Initial Velocity. Defaults to None.
        t (float, optional): Time. Defaults to None.
        a (float, optional): Acceleration. Defaults to None.
        x (float, optional): Displacement. Defaults to None.
        verbose (bool, optional): Printing To STDOUT and Verbose Error Handling. Defaults to False.

    Raises:
        ValueError: All values must be numeric.
        ValueError: There must be a single unknown value.
        ValueError: There can not be more than one unknown.

    Returns:
        float: Calculated Value for Unknown.
    """    
    result=0
    var = "x"

    try:
        vi = float(vi) if vi is not None else None 
        t = float(t) if t is not None else None
        a = float(a) if a is not None else None
        x = float(x) if x is not None else None
    except:
        raise ValueError(f"Non Numerics Passed as Values (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("Non Numerics Passed as Values")
    
    if x is not None: 
        if vi is None: 
            var = "vi"
            result = (x - ((1/2)*a*(t**2)))/t
        elif t is None:
            var = "t"
            result = math.sqrt((2 * (x - (vi * t))) / a)
        elif a is None:
            var = "a"
            result = (2 * (x - (vi * t))) / (t**2)
        else: 
            raise ValueError(f"No Unknowns Passed (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("No Unknowns Passed")
    else: 
        if vi is None or t is None or a is None:
            raise ValueError(f"Too Many Unknowns (vi,t,a,x):({vi},{t},{a},{x})") if verbose else ValueError("Too Many Unknowns")
        result = (vi * t) + ((1/2)*a*(t**2))

    if verbose:
        print(f"displacement: {var} = {result}")

    return result

if __name__ == "__main__":
    displacement(
        x=5,
        t=6.5,
        a=-1.4,
        verbose=True
        )