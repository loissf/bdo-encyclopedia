<template>
  <div class="item">
    <ItemIcon
      :item-id="item.id"
      :item-grade="item.grade"
      :enhancement="item.enhancement"
      :title="`${enhancementName} ${item.name}`"
    />
  </div>
</template>

<script setup lang="ts">
import { getEnhancementName } from "../utils/item-functions";

import ItemIcon from "@/components/ItemIcon.vue";

import { Item } from "./Process";
import { computed } from "vue";

const props = defineProps({
  item: {
    type: Object as () => Item,
    required: true,
  },
});

const enhancementName = computed(() =>
  getEnhancementName(props.item.id, props.item.enhancement)
);
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.item {
  display: flex;

  align-items: center;
  justify-content: center;

  width: 3.5rem;
  height: 3.5rem;

  padding: 0.75rem;

  border-radius: 12px;

  background-color: #2b2b2b;
  box-shadow: 4px 4px 12px 0px rgba(0, 0, 0, 0.75);

  .symbol-icon {
    position: absolute;
    width: 2.75rem;
  }
}
</style>
