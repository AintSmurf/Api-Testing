DELETE FROM wp_posts where post_type='shop_coupon' and post_title='test_coupon';
DELETE FROM wp_postmeta where post_id = 99999;
DELETE FROM wp_users WHERE user_email LIKE '%@test.com';
