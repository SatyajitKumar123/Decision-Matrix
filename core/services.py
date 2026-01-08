def calculate_pyramid_data(tasks, total_daily_hours):
    """
    Logic:
    1. Sum all task scores to get the 'Market Cap' (Total Context Score).
    2. Each task's weight = Task Score / Total Context Score.
    3. Allocate Time = Total Daily Hours * Weight.
    """

    # 1. Calculate the 'Market Cap' (Sum of all scores)
    total_context_score = sum(task.total_score for task in tasks)
    
    # Safety check: If user has 0 points total, avoid DivisionByZero error
    if total_context_score == 0:
        return []
    
    processed_tasks = []
    
    for task in tasks:
        # 2. Calculate Weight (The Asset Percentage)
        # Formula: (Score / Total) * 100
        weight_percent = (task.total_score / total_context_score) * 100
        
        # 3. Calculate Time Allocation
        # Formula: Total Hours * (Percent / 100)
        allocated_hours = total_daily_hours * (weight_percent / 100)

        # This disconnects us from the database model, which is faster for reading
        task_data = {
            'id': task.id,
            'title': task.title,
            'total_score': task.total_score,
            'weight_percent': round(weight_percent, 1),
            'allocated_hours': round(allocated_hours, 2)
        }
        processed_tasks.append(task_data)
    
    # 4. Sort by Score (Descending) - Essential for the Pyramid Visual
    # The highest score must be first (Top of pyramid)
    processed_tasks.sort(key=lambda x: x['total_score'], reverse=True)

    return processed_tasks
    