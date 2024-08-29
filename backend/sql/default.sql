INSERT INTO local.wp_posts (
    ID, post_author, post_date, post_date_gmt, post_content, post_title, 
    post_excerpt, post_status, comment_status, ping_status, post_password, 
    post_name, to_ping, pinged, post_modified, post_modified_gmt, 
    post_content_filtered, post_parent, guid, menu_order, post_type, 
    post_mime_type, comment_count
) VALUES (
    100000, 1, NOW(), NOW(), '', 
    'test_coupon', '', 'publish', 'closed', 'closed', '', 'test_coupon', 
    '', '', NOW(), NOW(), '', 0, 
    'http://testsite.local/?post_type=shop_coupon&#038;p=1000001', 0, 
    'shop_coupon', '', 0
);
