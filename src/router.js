import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/View/Home.vue'
import Course from '@/View/Course.vue'
import Project from '@/View/Project.vue'
import Enroll from '@/View/Enroll.vue'
import Login from '@/View/Login.vue'
import Blog from '@/View/Blog.vue'
import Topic from '@/View/Topic.vue'
import Question from '@/View/Question.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/project',
      name: 'project',
      component: Project
    },
    {
      path: '/enroll',
      name: 'enroll',
      component: Enroll
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog
    },
    {
      path: '/topic',
      name: 'topic',
      component: Topic
    },
    {
      path: '/questions',
      name: 'question',
      component: Question
    },
  ]
})
