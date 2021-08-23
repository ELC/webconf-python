<template>
  <div class="container">
    <header>
      <h1>Task Tracker</h1>
      <Button
        @btn-click="toggleAddTask()"
        :text="showAddTask ? 'Close' : 'Add'"
        :color="showAddTask ? 'red' : 'green'"
      />
    </header>

    <Main :showAddTask="showAddTask" />
    <footer>
      <p>Copyright &copy; 2021</p>
    </footer>
  </div>
</template>

<script>
import Main from './views/Main'

export default {
  name: 'App',
  props: {
    showAddTask: {
      type: Boolean,
      default: false
    },
  },
  components: {
    Main,
  },
  data() {
    return {
      showAddTask: false,
    }
  },
  methods: {
    toggleAddTask() {
      this.showAddTask = !this.showAddTask
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%;
}

footer {
  margin-top: 30px;
  text-align: center;
}
</style>
