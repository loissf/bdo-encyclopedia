<template>
  <div :grade="item.grade" class="item" :id="item.id.toString()">
    <ItemIcon
      :item-id="item.id"
      :item-grade="item.grade"
      :enhancement="enhancement"
    />
    <ItemName
      :item-id="item.id"
      :item-name="item.name"
      :item-grade="item.grade"
      :enhancement="enhancement"
    />
    <div class="price details-section">
      <label for="price-value">Base Price</label>
      <span class="value" id="price-value"
        ><img class="silver-icon" src="https:\\cdn.arsha.io/icons/1.png" />{{
          price
        }}</span
      >
    </div>
    <div class="stock details-section">
      <label for="stock-value">In Stock</label>
      <span class="value" id="stock-value">{{ item.stock }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { ListItem, SubListItem } from "@/models/Item";
import ItemIcon from "@/components/ItemIcon.vue";
import ItemName from "@/components/ItemName.vue";

const props = defineProps({
  item: {
    type: Object as () => ListItem | SubListItem,
    required: true,
  },
});

const price = computed(() => {
  const size = props.item.basePrice.toString().length;
  if (size > 9) {
    return parseFloat((props.item.basePrice / 1000000000).toFixed(2)) + " b";
  } else if (size > 6) {
    return parseFloat((props.item.basePrice / 1000000).toFixed(2)) + " M";
  } else if (size > 3) {
    return parseFloat((props.item.basePrice / 1000).toFixed(2)) + " k";
  }
});

function isSubListItem(item: any): item is SubListItem {
  if ((props.item as SubListItem).enhancement) {
    return true;
  }

  return false;
}

const enhancement = computed(() =>
  isSubListItem(props.item) ? props.item.enhancement : 0
);
</script>

<style scoped lang="scss">
.item {
  display: grid;

  grid-template: "icon name price stock" 1fr / 1fr 5fr 2fr 2fr;

  border: 1px solid rgba(255, 255, 255, 0.115);
  border-radius: 4px;
  box-shadow: 0px 0px 6px 0px rgba(0, 0, 0, 0.75);

  background-color: rgb(35, 35, 35);

  padding: 0.25rem;

  align-items: center;

  .item-icon {
    grid-area: icon;

    padding: 0.25rem;
    height: 2.5rem;
    width: 2.5rem;
  }

  .item-name {
    grid-area: name;
    padding: 0.5rem;
  }

  .price {
    grid-area: price;

    .silver-icon {
      height: 1.25rem;
      padding-right: 0.25rem;
    }
  }

  .stock {
    grid-area: stock;
  }

  .details-section {
    display: flex;
    flex-direction: column;

    justify-content: space-between;

    height: 100%;

    padding: 0 0.5rem;

    border-left: 1px solid rgb(70, 70, 70);

    label {
      text-align: left;
      font-size: 75%;
      color: rgba(255, 255, 255, 0.35);
    }

    .value {
      text-align: right;
    }
  }
}
</style>
