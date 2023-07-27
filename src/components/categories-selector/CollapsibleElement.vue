<template>
  <div class="collapsible-element">
    <div class="header" @click="toggleCollapse">
      <span class="title">{{ title }}</span>
      <span class="chevron" :class="collapsedStyle">&#8249;</span>
    </div>
    <div class="content" :class="collapsedStyle">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from "vue";

const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  categoryId: {
    type: String,
    required: true,
  },
  expanded: {
    type: String,
    required: false,
  },
});

watch(
  () => props.expanded,
  (value) => {
    if (value !== props.categoryId) {
      isCollapsed.value = true;
    }
  }
);

const isCollapsed = ref(true);

const collapsedStyle = computed(() =>
  isCollapsed.value ? "collapsed" : "expanded"
);

function toggleCollapse() {
  isCollapsed.value = !isCollapsed.value;
}
</script>

<style scoped lang="scss">
.collapsible-element {
  margin: 0.25rem;

  .header {
    padding: 0.625rem;

    display: flex;
    flex-direction: row;

    align-items: center;

    user-select: none;

    background-color: rgb(50, 50, 50);

    .title {
      flex-grow: 1;
      text-align: center;
    }

    .chevron {
      font-size: larger;
      &.expanded {
        transform: rotate(90deg);
      }
      &.collapsed {
        transform: rotate(270deg);
      }
    }

    &:hover {
      background-color: rgb(65, 65, 65);
    }
  }

  .content {
    display: flex;
    flex-direction: column;

    text-align: center;

    &.expanded {
      margin-top: 0.25rem;
    }

    &.collapsed {
      height: 0;
      overflow: hidden;
    }
  }
}
</style>
