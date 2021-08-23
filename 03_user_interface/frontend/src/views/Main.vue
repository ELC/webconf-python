<template>
  <AddTask v-show="showAddTask" @add-task="addTask" />
  <Tasks
    @delete-task="deleteTask"
    :tasks="tasks"
  />
</template>

<script>
import Tasks from '../components/Tasks'
import AddTask from '../components/AddTask'

export default {
  name: 'Main',
  props: {
    showAddTask: Boolean,
  },
  components: {
    Tasks,
    AddTask,
  },
  data() {
    return {
      tasks: [],
    }
  },
  methods: {
    async addTask(task) {
      const res = await fetch('/tasks', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(task),
      })

      const data = await res.json()

      this.tasks = [...this.tasks, data]
    },
    async deleteTask(id) {
      const res = await fetch(`/tasks/${id}`, {
        method: 'DELETE',
      })

      //We should control the response status to decide if we will change the state or not.
      res.status === 200
        ? (this.tasks = this.tasks.filter((task) => task.id !== id))
        : alert('Error deleting task')
    },
    async fetchTasks() {
      const res = await fetch('/tasks')

      const data = await res.json()

      return data
    }
  },
  async created() {
    this.tasks = await this.fetchTasks()
  },
}
</script>
