<template>
  <div class="item" :title="`${enhancementName} ${item.name}`">
    <img :src="iconUrl" id="icon" class="item-icon" :grade="item.grade" />
    <img :src="enhancementSymbolIcon" class="symbol-icon" />
  </div>
</template>

<script setup lang="ts">
import { getIconUrl } from "../utils/icon-functions";
import {
  getEnhancementName,
  getEnhancementSymbolIcon,
} from "../utils/grade-functions";

import { Item } from "./Process";
import { computed } from "vue";

const props = defineProps({
  item: {
    type: Object as () => Item,
    required: true,
  },
});

const iconUrl = computed(() => getIconUrl(props.item.id));

const enhancementName = computed(() =>
  getEnhancementName(props.item.id, props.item.enhancement)
);

const enhancementSymbolIcon = computed(() =>
  getEnhancementSymbolIcon(props.item.id, props.item.enhancement)
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
    width: 2.5rem;
  }
}
</style>
