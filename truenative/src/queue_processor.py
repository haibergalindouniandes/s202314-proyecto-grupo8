import queue
import multiprocessing


task_queue = multiprocessing.Queue()
process:multiprocessing.Process = None


def queue_executor(task_queue):
    while True:
        try:
            # Obtenemos la tarea de la cola
            task_id, executor = task_queue.get(timeout=1)
            result = executor(task_id)
            if not result:
                # Encolamos nuevamente si la tarea debe ser procesada nuevamente
                task_queue.put((task_id, executor))
        except queue.Empty:
            # Si la cola está vacía, salimos del bucle
            break


def enqueue_task(task_id:str, executor: any) -> None:
    # Encolamos tareas
    task_queue.put((task_id, executor))
    global process

    if process is None or not process.is_alive():
        # Creamos un proceso para ejecutar la cola
        process = multiprocessing.Process(target=queue_executor, args=(task_queue,))
        process.start()
