import hyperdiv as hd
from .tasks_state import TaskState


import time 

def timer_function(state):
    initial_time = time.time()
    elapsed_time = 0
    while state.task_running:
        time.sleep(1)
        elapsed_time += 1
        state.elapsed_time = elapsed_time

def header():
    """
    The header containing the "complete all" button and input form.
    """
    tasks = TaskState()
    with hd.hbox(
        padding=1,
        gap=1,
        align="center",
        border_bottom="1px solid neutral-200",
    ):

        state_stopwatch = hd.state(elapsed_time=0, task_running=False)

        # Input form
        with hd.form(direction="horizontal") as form:
            with hd.box():
                t1 = form.text_input(
                    name="new-task",
                    placeholder="Task name?",
                )

            with hd.box():
                if t1.value and not state_stopwatch.task_running:
                    form.submit_button("Add", variant="success")
                elif t1.value and state_stopwatch.task_running:
                    kwargs = dict(
                        border="1px solid red-300",
                        font_color="red",
                        background_color="red-50",
                    )

                    if hd.button("Stop", **kwargs).clicked:
                        tasks.add_task(t1.value, int(state_stopwatch.elapsed_time))
                        state_stopwatch.elapsed_time = 0
                        state_stopwatch.task_running = False
                        form.reset()

            with hd.box():
                if t1.value and state_stopwatch.task_running:
                    kwargs = dict(
                        border="1px solid green-300",
                        font_color="green",
                        background_color="green-50",
                    )

                    hd.button(state_stopwatch.elapsed_time, border_radius="circle", **kwargs)


        if form.submitted:
            task_name = form.form_data["new-task"]
            if task_name:
                state_stopwatch.elapsed_time = 0
                state_stopwatch.task_running = True
                task = hd.task() 
                task.rerun(timer_function, state_stopwatch)


def task_row(task,  duration, last_item=False):
    """
    Renders a task row. The check/unckeck button, the task name
    """
    tasks = TaskState()

    with hd.hbox(
        padding=1,
        gap=1,
        align="center",
        border_bottom=(None if last_item else "1px solid neutral-200"),
    ):
        hd.text(f"{task} ({duration} seconds)", grow=1, font_color="neutral-800")


def nothing_here():
    """
    This is rendered when there are no tasks to render.
    """
    with hd.box(padding=1.5, align="center", justify="center"):
        hd.text("There are no tasks here.", font_color="neutral-500")


def tasks_list():
    """
    Renders the list of tasks; 
    or the nothing_here component if there are no tasks.
    """
    tasks = TaskState()
    task_items = tasks.tasks

    if task_items:
        with hd.box(vertical_scroll=True):
            for i, (task, duration) in enumerate(task_items):
                with hd.scope(task):
                    task_row(task, duration, last_item=i == len(task_items) - 1)
    else:
        nothing_here()

def main():
    app = hd.template(title="Task Stopwatch App", sidebar=False)
    app.body.align = "center"
    with app.body:
        with hd.box(
            background_color="neutral-50",
            border="1px solid neutral-200",
            width=40,
            border_radius="large",
            vertical_scroll=False,
        ):
            header()
            tasks_list()
