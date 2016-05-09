"""
Simulator for greedy boss scenario
"""

import simpleplot
import math
import codeskulptor
codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    You can use plot_type to control whether regular or log/log plot
    """

    # initialize necessary local variables
    _current_earnings = 0
    _current_day = 0
    _bribes_paid = 0
    _current_salary = INITIAL_SALARY
    _current_bribe_cost = INITIAL_BRIBE_COST
    
    # define  list consisting of days vs. total salary earned for analysis
    _days_vs_earnings = []

    # each iteration of this while loop simulates one bribe
    while _current_day <= days_in_simulation:
        
        # update list with days vs total salary earned
        if plot_type:
            _days_vs_earnings.append((_current_day, _current_earnings))
        else:
            _days_vs_earnings.append((math.log(_current_day, 10), math.log(_current_earnings, 10)))
        
        # check whether we have enough money to bribe without waiting
        _money_needed = _current_bribe_cost - ( _current_earnings - _bribes_paid )
        if _money_needed <= 0:
            _days_needed = 0
        else:
            _days_needed = _money_needed // _current_salary
            if ( _money_needed % _current_salary ) != 0:
                _days_needed += 1
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        _current_day += _days_needed
        
        # update state of simulation to reflect bribe
        _bribes_paid += _current_bribe_cost
        _current_earnings += _days_needed * _current_salary
        _current_salary += SALARY_INCREMENT
        _current_bribe_cost += bribe_cost_increment
        
    return _days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = LOGLOG
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                         ["Bribe increment = 0", "Bribe increment = 500",
                          "Bribe increment = 1000", "Bribe increment = 2000"])

run_simulations()

print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]


            
            
    