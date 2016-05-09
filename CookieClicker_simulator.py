"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 100.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        Initialize a ClicckerState object
        """
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time_sec = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        output = "History recorded (time, item, price, total cookies produced):\n"
        for _index in range(len(self._history)):
            output += str(self._history[_index]) + "\n"
        output += "\n"
        output += ("Total number of cookies produced    = " + str(self._total_cookies) + "\n" +
                   "Current number of cookies available = " + str(self._current_cookies) + "\n" +
                   "Current time in seconds             = " + str(self._current_time_sec) + "\n" +
                   "Current CPS (Cookies Per Second)    = " + str(self._current_cps)) + "\n"
        return output
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time_sec
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        _cookies_needed = cookies - self._current_cookies
        if _cookies_needed <= 0:
            _time = 0.0
        else:
            _time = float( math.ceil( _cookies_needed / self._current_cps) )
        return _time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._current_time_sec += time
            self._current_cookies += time * self._current_cps
            self._total_cookies += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time_sec, item_name, cost, self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # Make a clone of the build_info object provided and
    # create ClickerState object for the game
    _my_build_info = build_info.clone()
    _my_game = ClickerState()
    
    while _my_game.get_time() <= duration:
        # Find out what the next buy must be
        _next_buy = strategy(_my_game.get_cookies(), _my_game.get_cps(),
                             _my_game.get_history(), (duration - _my_game.get_time()),
                             _my_build_info)
        if _next_buy == None:
            break
        
        # Find the time to wait to produce enough cookies to buy the item
        _time_needed = _my_game.time_until(_my_build_info.get_cost(_next_buy))
    
        # Wait until you have produced enough cookies
        if _my_game.get_time() + _time_needed > duration:
            break
        _my_game.wait(_time_needed)
        
        # Buy the item
        _my_game.buy_item(_next_buy, _my_build_info.get_cost(_next_buy),
                          _my_build_info.get_cps(_next_buy))
        
        # Update the item in the build_info object
        _my_build_info.update_item(_next_buy)
    
    # Use the time left to produce some more cookies
    _my_game.wait(duration - _my_game.get_time())
    
    return _my_game


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # Find the cheapest item in build_info
    _min = None
    _item_list = build_info.build_items()
    for _item in _item_list:
        _item_cost = build_info.get_cost(_item)
        if (_min == None) or (_min > _item_cost):
            _min = _item_cost
            _selected_item = _item
    
    # Check the chosen item for affordability
    if (_min == None) or (_min - cookies > time_left * cps):
        _selected_item = None
        
    return _selected_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    # Select the most expensive item you can afford
    _selected_item = None
    _max = 0
    _available = cookies + ( time_left * cps )
    _item_list = build_info.build_items()
    for _item in _item_list:
        _item_cost = build_info.get_cost(_item)
        if (_max < _item_cost) and (_item_cost <= _available):
            _max = _item_cost
            _selected_item = _item
        
    return _selected_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left
    but exclude "Time Machine" and "Antimatter Condenser".
    """
    # Find the item with the best cps / cost score in build_info
    _max = 0
    _item_list = build_info.build_items()
    for _item in _item_list:
        _item_cost = build_info.get_cost(_item)
        _item_cps = build_info.get_cps(_item)
        _cps_over_cost = _item_cps / _item_cost
        if (_max < _cps_over_cost):
            _max = _cps_over_cost
            _max_cost = _item_cost
            _selected_item = _item
    
    # Check the chosen item for affordability
    if (_max_cost - cookies > time_left * cps):
        _selected_item = None
        
    return _selected_item

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Best", SIM_TIME, strategy_best)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

